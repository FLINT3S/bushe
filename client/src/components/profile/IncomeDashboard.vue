<template>
  <div class="dashboard">
    <apexchart type="bar" :options="options.options" :series="options.series"></apexchart>
  </div>
</template>

<script lang="ts" setup>
interface Props {
  weekIncome: {
    monday: number,
    tuesday: number,
    wednesday: number,
    thursday: number,
    friday: number,
    saturday: number,
    sunday: number
  }
}
const props = defineProps<Props>()

const options = {
  options: {
    chart: {
      id: 'vuechart-example',
      offsetY: 4
    },
    xaxis: {
      categories: ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
    },
    yaxis: {
      labels: {
        show: false,
      },
      lines: {
        show: false
      }
    }
  },
  series: [{
    name: 'series-1',
    data: [props.weekIncome.monday, props.weekIncome.tuesday, props.weekIncome.wednesday, props.weekIncome.thursday, props.weekIncome.friday, props.weekIncome.saturday, props.weekIncome.sunday]
  }],
}
</script>