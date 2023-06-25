<template>
    <div class="container">
        <n-h1 class="mb-2">управление задачами</n-h1>

        <n-divider class="mt-2"/>

        <n-input v-model:value="searchQuery" class="mb-3" placeholder="Поиск по задачам"/>

        <div v-if="filteredTasks.length >= 1 || loading">
            <div v-if="!loading" class="row">
                <div v-for="(deliveryTaskItem, index) in filteredTasks" class="col-12 col-lg-6 col-xl-4">
                    <delivery-task-card @update="fetchActiveTasks" :delivery-task-item="deliveryTaskItem" change-status disable-status/>
                    <n-divider v-if="index < filteredTasks.length - 1"/>
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

        <n-button class="mt-3" block type="primary" @click="onClickLogout">
            Выйти

            <template #icon>
                <n-icon :component="LogoutIcon"/>
            </template>
        </n-button>
    </div>
</template>

<script lang="ts" setup>
import DeliveryTaskCard from "@components/deliveryTask/DeliveryTaskCard.vue";
import {DeliveryTask} from "@data/models/DeliveryTask";
import EmptyIcon from "@shared/ui/icon/EmptyIcon.vue";
import {apiInstance} from "@shared/api/apiInstance";
import {plainToInstance} from "class-transformer";
import LogoutIcon from "@shared/ui/icon/LogoutIcon.vue";

const deliveryTasks = ref<DeliveryTask[]>([])
const loading = ref(true)
const router = useRouter()

const searchQuery = ref("")

const onClickLogout = () => {
    router.push("/logout")
}

const filteredTasks = computed(() => {
    return deliveryTasks.value.filter(t => {
        return t.user.fullName.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
            t.orders.some(o => o.address.toLowerCase().includes(searchQuery.value.toLowerCase()))
    })
})

const fetchActiveTasks = () => {
    apiInstance.get("/delivery-task/active")
        .then((r) => {
            deliveryTasks.value = r.data.map((t: any) => plainToInstance(DeliveryTask, t))
        })
        .finally(() => {
            loading.value = false
        })
}


onMounted(() => {
    fetchActiveTasks()
})
</script>

<style scoped>

</style>