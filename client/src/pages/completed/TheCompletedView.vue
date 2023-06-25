<template>
  <div class="container">
    <n-h1 class="mb-2">завершенные</n-h1>
    <n-divider class="mt-2"/>
    <OrderHistoryButton>назад в профиль</OrderHistoryButton>
    <div class="empty"></div>
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

      <h3 class="mt-4" style="color: #CACDD0">для вас пока нет доставок :(</h3>
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
import EmptyIcon from "@shared/ui/icon/EmptyIcon.vue";
import OrderHistoryButton from "@shared/components/OrderHistoryButton.vue";

const router = useRouter()
const message = useMessage()
const {currentUser} = storeToRefs(useUserStore())
const deliveryTasks = ref<DeliveryTask[]>([])
const loading = ref(true)

onMounted(() => {
  apiInstance.post("/auth/check", {accessToken: localStorage.getItem(LocalStorageKeys.ACCESS_TOKEN)})
      .then(response => {
        currentUser.value = plainToInstance(CurrentUser, response.data)
        apiInstance.get(`/delivery-task/resolved/${currentUser.value.id}`)
            .then((r) => {
              deliveryTasks.value = r.data.map((d: any) => plainToInstance(DeliveryTask, d)).filter((d: DeliveryTask) => d.orders.length > 0)
            })
            .finally(() => {
              loading.value = false
            })
      })
      .catch(() => {
        localStorage.setItem(LocalStorageKeys.ACCESS_TOKEN, "")
        router.replace("/login")
      })
})
</script>

<style scoped>
.empty{margin-top: 10px;}
</style>