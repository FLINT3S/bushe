<template>
    <div class="container d-flex flex-column">
        <n-h1 class="mb-2">в процессе</n-h1>

        <n-divider class="mt-2"/>

        <div class="active-task-container d-flex flex-column mx-md-auto">
            <delivery-task-card v-if="activeDeliveryTask" :delivery-task-item="activeDeliveryTask" check-orders/>
            <n-skeleton v-else height="400px" width="100%"></n-skeleton>

            <n-button :loading="!activeDeliveryTask" size="large" class="mt-3 mx-auto" type="primary" @click="onClickApproveOrder">
                Заказ вручён клиенту
            </n-button>

            <div v-if="activeDeliveryTask" id="map" class="map mt-4" style="height: 400px"></div>
            <n-skeleton v-else class="mt-4" height="400px" width="100%"></n-skeleton>

            <a :href="'https://yandex.ru/maps/?text=' + activeOrder?.address"
                         class="mt-3 text-decoration-none" target="_blank">
                <n-button block secondary type="primary" :loading="!activeDeliveryTask">
                    Открыть в Яндекс.Картах
                </n-button>
            </a>
        </div>
    </div>
</template>

<script lang="ts" setup>
import deliveryTasks from "@/data/mock/deliveryTasks.json"
import {DeliveryTask} from "@data/models/DeliveryTask";
import {plainToInstance} from "class-transformer";
import DeliveryTaskCard from "@components/deliveryTask/DeliveryTaskCard.vue";
import {apiInstance} from "@shared/api/apiInstance";

const dialog = useDialog()
const message = useMessage()

const activeDeliveryTask = ref<DeliveryTask | null>(null)

const previousOrder = computed(() => {
    return activeDeliveryTask.value?.orders.slice().reverse().find(order => order.isCompleted)
})

const activeOrder = computed(() => {
    return activeDeliveryTask.value?.orders.find(order => !order.isCompleted)
})

const nextOrder = computed(() => {
    const activeOrderIndex = activeDeliveryTask.value?.orders.findIndex(order => order.id === activeOrder.value!.id)
    if (!activeOrderIndex || activeOrderIndex + 1 >= activeDeliveryTask.value?.orders?.length!) {
        return null
    }
    return activeDeliveryTask.value?.orders[activeOrderIndex + 1]
})

const fetchActiveOrder = () => {
    apiInstance.get("/")
    setTimeout(() => {
        activeDeliveryTask.value = plainToInstance(DeliveryTask, deliveryTasks[0])

        nextTick(() => {
            deliveryMap = new window.ymaps.Map('map', {
                center: [55.750625, 37.626],
                zoom: 7,
                controls: []
            }, {
                buttonMaxWidth: 300
            })

            nextTick(() => {
                // window.ymaps.ready(renderRoute);
            })
        })
    }, 1000)
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
    // Кинуть запрос что заказ доставлен

}

let deliveryMap = reactive<any>(null)

const renderRoute = () => {
    let multiRoute = new window.ymaps.multiRouter.MultiRoute({
        referencePoints: [
            previousOrder.value?.address,
            activeOrder.value?.address
        ],
        params: {
            results: 1
        }
    }, {
        boundsAutoApply: true
    });

    deliveryMap.geoObjects.add(multiRoute);
}

onMounted(() => {
    fetchActiveOrder()
})
</script>

<style lang="scss" scoped>
.active-task-container {
  @media screen and (min-width: 768px) {
    max-width: 576px;
    min-width: 450px;
  }
}
</style>