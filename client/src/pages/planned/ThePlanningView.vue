<template>
    <div class="container">
        <n-h1 class="mb-2">запланированные</n-h1>

        <n-divider class="mt-2"/>

        <div class="row" v-if="!loading">
            <div v-for="(deliveryTaskItem, index) in deliveryTasks" class="col-12 col-lg-6 col-xl-4">
                <delivery-task-card :delivery-task-item="deliveryTaskItem"/>
                <n-divider v-if="index < deliveryTasks.length - 1"/>
            </div>
        </div>

        <div class="row" v-else>
            <div v-for="i in 4" class="col-12 col-lg-6 col-xl-4">
                <n-skeleton width="100%" height="300px" class="mb-3"/>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import DeliveryTaskCard from "@components/deliveryTask/DeliveryTaskCard.vue";
import {DeliveryTask} from "@data/models/DeliveryTask";
import {plainToInstance} from "class-transformer"
import {apiInstance} from "@shared/api/apiInstance";
import {LocalStorageKeys} from "@shared/model/LocalStorageKeys";
import {storeToRefs} from "pinia";
import {useUserStore} from "@shared/model/store/useUserStore";
import {CurrentUser} from "@data/models/CurrentUser";

const router = useRouter()
const message = useMessage()
const {currentUser} = storeToRefs(useUserStore())
const deliveryTasks = ref<DeliveryTask[]>([])
const loading = ref(true)

onMounted(() => {
    apiInstance.post("/auth/check", {accessToken: localStorage.getItem(LocalStorageKeys.ACCESS_TOKEN)})
        .then(response => {
            currentUser.value = plainToInstance(CurrentUser, response.data)
            apiInstance.get(`/delivery-task/getUserTasks/${currentUser.value?.id}`).then((r) => {
                deliveryTasks.value = r.data.map((d: any) => plainToInstance(DeliveryTask, d)).filter((d: DeliveryTask) => d.orders.length > 0)
            })
        })
        .catch(() => {
            localStorage.setItem(LocalStorageKeys.ACCESS_TOKEN, "")
            router.replace("/login")
        })
        .finally(() => {
            loading.value = false
        })
})
</script>

<style scoped>

</style>