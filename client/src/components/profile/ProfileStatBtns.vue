<template>
  <div class="row row-cols-2">
    <div class="col">
      <n-card size="large">
            Доставлено в этом месяце: {{stats.deliveriedMonth}}
      </n-card>
    </div>
    <div class="col">
      <n-card size="large">
            Заработано в этом месяце: {{stats.earnedMonth}}
      </n-card>
    </div>
    <div class="col">
      <n-card size="large">
            Доставлено всего: {{stats.deliveriedTotal}}
      </n-card>
    </div>
    <div class="col">
      <n-card size="large">
            Заработано всего: {{stats.deliveriedTotal}}
      </n-card>
    </div>
  </div>
</template>

<script lang="ts" setup>
// import {apiInstance} from "@shared/api/apiInstance";
import axios from "axios";
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