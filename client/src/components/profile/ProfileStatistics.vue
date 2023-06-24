<template>
  <div class="stats__inner d-flex flex-column">
    <div class="stats-header">статистика</div>
    <div class="stats__widget">
      <StatisticWidget :mode="'заработано'" :values="stats.earned"/>
      <StatisticWidget :mode="'доставлено'" :values="stats.delivered"/>
      <OrderHistoryButton>история заказов</OrderHistoryButton>
    </div>
  </div>
</template>

<script lang="ts" setup>
// import {apiInstance} from "@shared/api/apiInstance";
import axios from "axios";
import StatisticWidget from "@components/profile/StatisticWidget.vue";
import {Ref} from "vue/dist/vue";
import {StatisticActionMode} from "@data/types/statisticActionMode";
import OrderHistoryButton from "@shared/components/OrderHistoryButton.vue";

// TODO: authStore получить значение стора из pinia
const authStore = {
  id: 1,
}
const courierId = computed(()=>{
  return authStore.id
})

// TODO: сделать запрос на статистику
let stats = ref({
  delivered: {
    perDay: 24,
    perMonth: 64
  },
  earned: {
    perDay: 1203,
    perMonth: 25178
  },
  income: {
    monday: 1492,
    tuesday: 1357,
    wednesday: 1518,
    thursday: 1646,
    friday: 1203,
    saturday: 0,
    sunday: 0
  }
})

onMounted(async ()=>{
  const statsRes = await axios.get('https://run.mocky.io/v3/8d5c6937-1efa-4a07-9bdb-1654a46010f8')
  if(statsRes) {
    stats.value = statsRes.data
  }
})

</script>

<style scoped>
.stats-header {
  font-size: 16px;
  line-height: 100%;
  margin-top: 29px;
  margin-bottom: 15px;
}
</style>