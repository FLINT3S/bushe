<template>
    <div class="container">
        <n-h1 class="mb-2">управление задачами</n-h1>

        <n-divider class="mt-2"/>

        <div v-if="deliveryTasks.length >= 1 || loading">
            <div v-if="!loading" class="row">
                <div v-for="(deliveryTaskItem, index) in deliveryTasks" class="col-12 col-lg-6 col-xl-4">
                    <delivery-task-card :delivery-task-item="deliveryTaskItem"/>
                    <n-divider v-if="index < deliveryTasks.length - 1"/>
                </div>
            </div>

            <div v-else class="row">
                <div v-for="i in 4" class="col-12 col-lg-6 col-xl-4">
                    <n-skeleton class="mb-3" height="300px" width="100%"/>
                </div>
            </div>
        </div>

        <div v-else class="d-flex justify-content-center text-center align-items-center mt-4 flex-column">
            <EmptyIcon/>

            <h3 class="mt-4" style="color: #CACDD0">пока что нет активных задач :(</h3>
        </div>
    </div>
</template>

<script lang="ts" setup>
import DeliveryTaskCard from "@components/deliveryTask/DeliveryTaskCard.vue";
import {DeliveryTask} from "@data/models/DeliveryTask";
import EmptyIcon from "@shared/ui/icon/EmptyIcon.vue";

const deliveryTasks = ref<DeliveryTask[]>([])
const loading = ref(true)

const fetchActiveTasks = () => {
    console.log(123)
}

onMounted(() => {
    fetchActiveTasks()
})
</script>

<style scoped>

</style>