<template>
  <div class="container">
    <div class="col" v-if='stats'>
      <n-h1 class="mb-2">личный кабинет</n-h1>

      <n-divider class="mt-2"/>
      <div class="profile-section row-cols-1">
        <profile-card />
      </div>

      <div class="profile-section row-cols-1">
        <ProfileStatistics :stats="stats"/>
      </div>

      <div class="profile-section row-cols-1">
        <ProfileIncome :stats="stats"/>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import ProfileCard from "@/components/profile/ProfileCard.vue"
import ProfileStatistics from "@components/profile/ProfileStatistics.vue";
import ProfileIncome from "@components/profile/ProfileIncome.vue"
import {useUserStore} from "@shared/model/store/useUserStore";
import {apiInstance} from "@shared/api/apiInstance";

// let stats = ref({
//   delivered: {
//     perDay: 24,
//     perMonth: 64
//   },
//   earned: {
//     perDay: 1203,
//     perMonth: 25178
//   },
//   income: {
//     monday: 1492,
//     tuesday: 1357,
//     wednesday: 1518,
//     thursday: 1646,
//     friday: 1203,
//     saturday: 0,
//     sunday: 0
//   }
// })
const stats = ref(null)
const router = useRouter()
const userStore = useUserStore()
const courierId = userStore.currentUser?.id


onMounted(async ()=>{
  if (![1, 3].includes(userStore.currentUser!.role)) {
      await router.replace("/manageOrders")
      return
  }

  const statsRes = await apiInstance.get(`/user/statistics/${courierId}`)
  if(statsRes) {
    stats.value = statsRes.data
  }
})
</script>

<style lang="scss" scoped>
.profile-header{
  font-size: 32px;
  width: 100%;
  line-height: 100%;

}
</style>