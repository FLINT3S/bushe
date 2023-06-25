<template>
    <div class="container d-flex flex-column">
        <n-h1 class="mb-2">в процессе</n-h1>

        <n-divider class="mt-2"/>

        <div v-if="activeDeliveryTask || loading" class="active-task-container d-flex flex-column mx-md-auto">
            <delivery-task-card v-if="activeDeliveryTask && !loading" :delivery-task-item="activeDeliveryTask!" check-orders/>
            <n-skeleton v-else height="400px" width="100%"></n-skeleton>

            <div v-if="!nextOrder" class="text-center mt-3">
                <n-h2 class="mb-2">Все заказы доставлены!</n-h2>
                <n-h4 class="mt-0">Возвращайтесь на точку</n-h4>

                <n-button size="large" type="primary" @click="onClickEndDelivery">
                    Закончить доставку
                </n-button>
            </div>

            <n-button v-if="nextOrder" :loading="!activeDeliveryTask" class="mt-3 mx-auto" size="large"
                      type="primary" @click="onClickApproveOrder">
                Заказ вручён клиенту
            </n-button>

            <n-spin :show="!activeDeliveryTask || !routeCreated">
                <div id="map" class="map mt-4" style="height: 400px"></div>
            </n-spin>

            <a :href="'https://yandex.ru/maps/?text=' + toAddress"
               class="mt-3 text-decoration-none" target="_blank">
                <n-button :loading="!activeDeliveryTask" block secondary type="primary">
                    Открыть в Яндекс.Картах
                </n-button>
            </a>
        </div>

        <div v-else class="d-flex justify-content-center text-center align-items-center mt-4 flex-column">
            <EmptyIcon/>

            <h3 class="mt-4" style="color: #CACDD0">для вас пока нет доставок :(</h3>
        </div>
    </div>
</template>

<script lang="ts" setup>
import {DeliveryTask} from "@data/models/DeliveryTask";
import {plainToInstance} from "class-transformer";
import DeliveryTaskCard from "@components/deliveryTask/DeliveryTaskCard.vue";
import {apiInstance} from "@shared/api/apiInstance";
import {storeToRefs} from "pinia";
import {useUserStore} from "@shared/model/store/useUserStore";
import {LocalStorageKeys} from "@shared/model/LocalStorageKeys";
import {CurrentUser} from "@data/models/CurrentUser";
import EmptyIcon from "@shared/ui/icon/EmptyIcon.vue";

const dialog = useDialog()
const router = useRouter()
const message = useMessage()
const {currentUser} = storeToRefs(useUserStore())
const activeDeliveryTask = ref<DeliveryTask | null>(null)
const loading = ref(true)

const previousOrder = computed(() => {
    return activeDeliveryTask.value?.orders.slice().reverse().find(order => order.isCompleted)
})

const activeOrder = computed(() => {
    return activeDeliveryTask.value?.orders.find(order => !order.isCompleted)
})

const nextOrder = computed(() => {
    if (activeDeliveryTask.value?.orders?.every(order => order.isCompleted)) {
        return null
    }

    const activeOrderIndex = activeDeliveryTask.value?.orders?.findIndex(order => order?.id === activeOrder.value?.id)
    if ((!activeOrderIndex && activeOrderIndex !== 0) || activeOrderIndex > activeDeliveryTask.value?.orders?.length!) {
        return null
    }

    return activeDeliveryTask.value?.orders[activeOrderIndex]
})

const fromAddress = computed(() => {
    if (!previousOrder?.value?.address) {
        return activeOrder.value?.restaurant_address
    }

    return previousOrder.value.address
})

const toAddress = computed(() => {
    if (activeDeliveryTask.value?.orders?.every(order => order.isCompleted)) {
        return activeDeliveryTask.value?.orders?.[0]?.restaurant_address
    }

    return activeOrder.value?.address
})

const fetchActiveOrder = async () => {
    loading.value = true

    const res = await apiInstance.get(`/delivery-task/getUserActiveTask/${currentUser.value?.id}`)
    if (!res) {
        activeDeliveryTask.value = null
    }
    activeDeliveryTask.value = plainToInstance(DeliveryTask, res.data)

    await nextTick(() => {
        window.ymaps.ready(renderRoute);
    })

    loading.value = false
}

const onClickApproveOrder = () => {
    dialog.warning({
        title: "Завершить заказ?",
        content: "Подтверждаю, что заказ отдан клиенту",
        positiveText: 'Да',
        negativeText: 'Отмена',
        onPositiveClick: () => {
            message.success('Заказ отмечен, как выполненный')
            onClickConfirmApproveOrder()
        },
        onNegativeClick: () => {
        }
    })
}

const onClickConfirmApproveOrder = () => {
    apiInstance.get(`/order/completeOrder/${activeOrder.value?.id}`)
        .then(() => {
            fetchActiveOrder()
        })
        .catch((e) => {
            message.error(`Ошибка подтверждения заказа: ${e.message}`)
        })

}

const onClickEndDelivery = () => {
    dialog.warning({
        title: "Завершить доставку?",
        positiveText: 'Завершить',
        negativeText: 'Отмена',
        onPositiveClick: () => {
            message.success('Доставка завершена!')
            onClickConfirmApproveEndDelivery()
        },
        onNegativeClick: () => {
        }
    })
}

const onClickConfirmApproveEndDelivery = () => {
    apiInstance.get(`/delivery-task/finish/${activeDeliveryTask.value?.id}`)
        .then(() => {
            router.replace("/profile")
        })
}

let deliveryMap = reactive<any>(null)
const routeCreated = ref(false)

const renderRoute = () => {
    let multiRoute = new window.ymaps.multiRouter.MultiRoute({
        referencePoints: [
            fromAddress.value,
            toAddress.value
        ],
        params: {
            results: 1
        }
    }, {
        boundsAutoApply: true
    });

    multiRoute.model.events.add('requestsuccess', () => {
        setTimeout(() => {
            routeCreated.value = true
        }, 200)
    })

    nextTick(() => {
        deliveryMap?.geoObjects?.removeAll();
        deliveryMap?.geoObjects?.add(multiRoute);
    })
}

onMounted(() => {
    apiInstance.post("/auth/check", {accessToken: localStorage.getItem(LocalStorageKeys.ACCESS_TOKEN)})
        .then(response => {
            currentUser.value = plainToInstance(CurrentUser, response.data)

            fetchActiveOrder()
        })
        .catch(() => {
            localStorage.setItem(LocalStorageKeys.ACCESS_TOKEN, "")
            router.replace("/login")
        })
})

watch(activeDeliveryTask, () => {
    nextTick(() => {
        try {
            if (!document.querySelector("#map")?.children?.length) {
                deliveryMap = new window.ymaps.Map('map', {
                    center: [55.750625, 37.626],
                    zoom: 7,
                    controls: []
                }, {
                    buttonMaxWidth: 300
                })
            }
        } catch (e) {
            console.log(e)
        }
    })
})

onBeforeUnmount(() => {
    deliveryMap?.destroy()
})
</script>

<style lang="scss" scoped>
.active-task-container {
  @media screen and (min-width: 768px) {
    max-width: 520px;
    min-width: 520px;
  }
}
</style>