<template>
    <div>
        <div class="d-flex justify-content-between mb-3">
            <n-h4 class="mb-0">доставка {{ deliveryTaskItem.id }}</n-h4>
            <n-button v-if="!disableStatus" class="text-decoration-underline" text type="primary">
                {{ deliveryTaskItem.status.name }}
            </n-button>
        </div>

        <n-card>
            <div v-for="(deliveryTaskOrder, index) in deliveryTaskItem.orders"
                 :class="{'mb-4': index < deliveryTaskItem.orders.length - 1}"
            >
                <div class="d-flex align-items-center">
                    <arrow-right-icon/>

                    <span class="ms-2">
                        заказ {{ deliveryTaskOrder.id }}
                    </span>

                    <span class="ms-auto">
                        {{ deliveryTaskOrder.deadlineFormat }}
                    </span>
                </div>

                <div class="d-flex justify-content-between align-items-center mt-2 text-wrap">
                    <div>
                        {{ deliveryTaskOrder.address }}
                    </div>

                    <div v-if="checkOrders">
                        <n-checkbox :checked="deliveryTaskOrder.isCompleted"/>
                    </div>
                </div>
            </div>

            <div v-if="changeStatus" class="mt-3">
                <n-h3>Исполнитель: {{ deliveryTaskItem.user.fullName }}</n-h3>

                <n-select :options="statusOptions" v-model:value="deliveryTaskItem.status.id" class="mt-3"
                          placeholder="Статус доставки"/>

                <n-button block class="mt-2" secondary type="primary" @click="onClickSaveStatus">
                    Сохранить
                </n-button>
            </div>
        </n-card>
    </div>
</template>

<script lang="ts" setup>
import ArrowRightIcon from "@shared/ui/icon/ArrowRightIcon.vue";
import {DeliveryTask} from "@data/models/DeliveryTask";
import {apiInstance} from "@shared/api/apiInstance";

interface Props {
    deliveryTaskItem: DeliveryTask,
    checkOrders?: boolean,
    disableStatus?: boolean,
    changeStatus?: boolean
}

const props = withDefaults(defineProps<Props>(), {
    checkOrders: false,
    disableStatus: false,
    changeStatus: false
})

const emit = defineEmits(["update"])

const statusOptions = [
    {
        label: "Назначено",
        value: 1
    },
    {
        label: "Готовится",
        value: 2
    },
    {
        label: "Ожидает выдачи",
        value: 3
    },
    {
        label: "В доставке",
        value: 4
    }
]

const onClickSaveStatus = () => {
    apiInstance.post("/delivery-task/change-status", {
        delivery_task_id: props.deliveryTaskItem.id,
        new_status_id: props.deliveryTaskItem.status.id
    }).then(() => {
        emit("update")
    })
}
</script>

<style scoped>

</style>