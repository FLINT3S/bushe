<template>
    <div>
        <div style="overflow: auto">
            <n-data-table
                scroll-x="600"
                    v-model:checked-row-keys="selectedOrdersIds"
                    :columns="columns"
                    :data="orders"
                    :loading="loading"
                    :pagination="{
                        pageSize: 10
                    }"
                    :row-key="(rowData: Order) => rowData.id"
                    @update:filters="handleUpdateFilter"
            />
        </div>

        <n-divider/>

        <div class="row d-flex flex-column-reverse flex-md-row">
            <div class="col-12 col-md-6 mt-3 mt-md-0">
                <n-spin :show="loading || routeCreating">
                    <div id="manager_map" style="height: 500px"></div>
                </n-spin>
            </div>
            <div class="col-12 col-md-6">
                <n-h2 v-if="selectedOrdersIds.length">выбрано заказов: {{ selectedOrdersIds.length }}</n-h2>
                <n-h2 v-else>не выбрано ни одного заказа</n-h2>

                <n-h3 v-if="selectedOrdersIds.length" class="mt-4">общая масса заказов:
                    {{ (selectedOrders.reduce((acc, cur) => acc += cur.weight, 0) / 1000).toFixed(2) }}кг
                </n-h3>

                <div v-if="selectedOrdersIds.length">
                    <n-divider/>

                    <n-list>
                        <n-list-item v-for="(order, index) in selectedOrders">
                            {{ order.address.replaceAll("Санкт-Петербург, ", "") }} ({{ order.deadlineFormat }})
                        </n-list-item>
                    </n-list>

                    <n-button class="mt-4" type="primary" @click="createRoute">
                        проложить маршрут
                    </n-button>

                    <n-h2>длина маршрута: ~{{ (routeDistance / 1000).toFixed(2) }}км</n-h2>

                    <n-select v-model:value="selectedCourierId" :options="courierListSelect" class="mb-3"
                              placeholder="выбор курьера"/>

                    <n-button :disabled="!routeDistance || !selectedCourierId" type="primary"
                              @click="onClickSaveDeliveryTask">
                        сохранить доставку
                    </n-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import {Order} from "@data/models/Order";
import {DataTableBaseColumn, DataTableColumns, DataTableFilterState} from "naive-ui"
import {plainToInstance} from "class-transformer";
import {apiInstance} from "@shared/api/apiInstance";
import {storeToRefs} from "pinia";
import {useUserStore} from "@shared/model/store/useUserStore";
import {User} from "@data/models/User";

const orders = ref<Order[]>([])
const loading = ref(true)

const fetchInitData = () => {
    apiInstance.get("/order/getAll").then((r) => {
        orders.value = r.data.map((o: any) => plainToInstance(Order, o))
    }).finally(() => {
        loading.value = false
    })

    managerMap?.geoObjects?.removeAll();
}

onMounted(() => {
    fetchInitData()
})

const restaurantColumn = reactive({
    title: 'Пункт выдачи',
    key: 'restaurant_address',
    render(row: Order) {
        return row.restaurant_address.replace("Санкт-Петербург, ", "")
    },
    filterMultiple: false,
    filterOptionValue: "Невский просп., 114-116",
    filterOptions: [
        {
            label: 'Невский просп., 114-116',
            value: 'Невский просп., 114-116'
        },
        {
            label: 'наб. канала Грибоедова, 18-20',
            value: 'наб. канала Грибоедова, 18-20'
        },
        {
            label: 'Средний просп. Васильевского острова, 33',
            value: 'Средний просп. Васильевского острова, 33'
        },
        {
            label: 'Парадная ул., 3, корп. 2',
            value: 'Парадная ул., 3, корп. 2'
        },
        {
            label: 'ул. Льва Толстого, 1-3',
            value: 'ул. Льва Толстого, 1-3'
        },
        {
            label: 'Малая Морская ул., 7',
            value: 'Малая Морская ул., 7'
        },
    ],
    filter(value: any, row: Order) {
        return !!~row.restaurant_address.indexOf(value.toString())
    }
})

const columns: DataTableColumns<Order> = reactive<DataTableColumns<Order>>([
    {
        type: 'selection',
        disabled: (row) => {
            if (!selectedOrders.value.length) {
                return false
            }

            return selectedOrders.value?.[0]?.deadline.getDate() !== row.deadline.getDate()
        }
    },
    {
        title: "Время доставки",
        key: "deadline",
        sorter: (row1, row2) => row1.deadline.getTime() - row2.deadline.getTime(),
        defaultSortOrder: 'ascend',
        render(row) {
            return row.deadlineDateTimeFormat
        }
    },
    {
        title: 'Адрес доставки',
        key: 'address',
        render(row) {
            return row.address.replace("Санкт-Петербург, ", "")
        }
    },
    restaurantColumn,
    {
        title: 'Вес',
        key: 'weight',
        render(row) {
            return (row.weight / 1000).toFixed(2) + "кг"
        }
    }
])

const handleUpdateFilter = (
    filters: DataTableFilterState,
    sourceColumn: DataTableBaseColumn
) => {
    restaurantColumn.filterOptionValue = filters[sourceColumn.key] as string
}

const selectedOrdersIds = ref<number[]>([])
const onSelectRows = (v: number[]) => {
    selectedOrdersIds.value = v.slice()
}

const selectedOrders = computed(() => {
    return orders.value.filter((o: Order) => selectedOrdersIds.value.includes(o.id))
})

let managerMap = reactive<any>({})

onMounted(() => {
    try {
        if (!document.querySelector("#manager_map")?.children?.length) {
            managerMap = new window.ymaps.Map('manager_map', {
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

const routeCreating = ref(false)
const routeDistance = ref(0)

const createRoute = () => {
    routeCreating.value = true

    let multiRoute = new window.ymaps.multiRouter.MultiRoute({
        referencePoints: routePoints.value,
        params: {
            results: 1
        }
    }, {
        boundsAutoApply: true
    });

    multiRoute.model.events.add('requestsuccess', () => {
        setTimeout(() => {
            routeCreating.value = false

            const routes = multiRoute.getRoutes();
            for (let i = 0, l = routes.getLength(); i < l; i++) {
                const route = routes.get(i);
                routeDistance.value += route.properties.get('distance').value
            }
        }, 200)
    })


    nextTick(() => {
        managerMap?.geoObjects?.removeAll();
        managerMap?.geoObjects?.add(multiRoute);
    })
}

const routePoints = computed(() => {
    return [
        restaurantColumn.filterOptionValue,
        ...selectedOrders.value.map(o => o.address),
        restaurantColumn.filterOptionValue,
    ]
})

const {currentUser} = storeToRefs(useUserStore())

const onClickSaveDeliveryTask = () => {
    apiInstance.post("/delivery-task/create", {
        delivery_way_len: parseFloat((routeDistance.value / 1000).toFixed(2)),
        user_id: selectedCourierId.value,
        orders: selectedOrdersIds.value
    }).then(() => {
        fetchInitData()
        selectedCourierId.value = null as unknown as number
        routeDistance.value = 0

    })
}

const selectedCourierId = ref(null as unknown as number)
const couriersList = ref<User[]>([])

onMounted(() => {
    apiInstance.get("/user/getCouriers").then((r) => {
        couriersList.value = r.data.map((c: any) => plainToInstance(User, c))
    })
})

const courierListSelect = computed(() =>
    couriersList.value.map(c => ({
        label: c.fullName,
        value: c.id
    }))
)
</script>

<style scoped>

</style>