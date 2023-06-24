<template>
  <div class="stats__inner d-flex flex-column">
    <div class="stats-header">статистика</div>
    <div class="stats__widget">
      <StatisticWidget />
    </div>
  </div>
</template>

<script lang="ts" setup>
// import {apiInstance} from "@shared/api/apiInstance";
import axios from "axios";
import StatisticWidget from "@components/profile/StatisticWidget.vue";
// TODO: authStore получить значение стора из pinia
const authStore = {
  id: 1,
}
const courierId = computed(()=>{
  return authStore.id
})
let stats = ref({
  data: {
    deliveriedMonth: 24,
    deliveriedTotal: 638,
    earnedMonth: 6846,
    earnedTotal: 23178
  }
})

onMounted(async ()=>{
  const statsRes = await axios.get('https://run.mocky.io/v3/3fbab8a9-f654-4241-b305-73212eddfdf5')
  if(statsRes) {
    stats.value = statsRes.data
  }
})

</script>

<style scoped>
.stats-header {
  font-size: 16px;
}
</style>