<template>
    <div class="container">
        <n-h1 class="mb-2">запланированные</n-h1>

        <n-divider class="mt-2"/>

        <div class="row">
            <div v-for="(deliveryTaskItem, index) in deliveryTasks" class="col-12 col-lg-6 col-xl-4">
                <delivery-task-card :delivery-task-item="deliveryTaskItem"/>
                <n-divider v-if="index < deliveryTasks.length - 1"/>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import DeliveryTaskCard from "@components/deliveryTask/DeliveryTaskCard.vue";
import deliveryTasksMock from "@/data/mock/deliveryTasks.json"
import {DeliveryTask} from "@data/models/DeliveryTask";
import {plainToInstance} from "class-transformer"

const deliveryTasks = ref<DeliveryTask[]>([])

onMounted(() => {
    deliveryTasks.value = plainToInstance(DeliveryTask, deliveryTasksMock)
})
</script>

<style scoped>

</style>