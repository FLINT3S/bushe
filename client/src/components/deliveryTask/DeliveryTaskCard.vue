<template>
    <div>
        <div class="d-flex justify-content-between mb-3">
            <n-h4 class="mb-0">доставка {{ deliveryTaskItem.id }}</n-h4>
            <n-button class="text-decoration-underline" text type="primary">
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

                <div class="d-flex justify-content-between align-items-center mt-2">
                    <div>
                        {{ deliveryTaskOrder.address }}
                    </div>

                    <div v-if="checkOrders">
                        <n-checkbox :checked="deliveryTaskOrder.isCompleted"/>
                    </div>
                </div>
            </div>
        </n-card>
    </div>
</template>

<script lang="ts" setup>
import ArrowRightIcon from "@shared/ui/icon/ArrowRightIcon.vue";
import {DeliveryTask} from "@data/models/DeliveryTask";

interface Props {
    deliveryTaskItem: DeliveryTask,
    checkOrders?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  checkOrders: false
})
</script>

<style scoped>

</style>