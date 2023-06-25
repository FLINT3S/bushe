<template>
  <div class="dashboard">
    <apexchart type="bar" :options="options" :series="options.series"></apexchart>
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
const ind = ref(0);
const options = {
  // colors: ['#CACDD0'],
  colors: [
    function({ value, seriesIndex, w}: {value: any, seriesIndex: any, w: any}) {
    if (value > 7000) {
        return '#F0A72D'
      } else {
        return '#CACDD0'
      }
    }
  ],
  plotOptions: {
    bar: {
      dataLabels: {
        position: 'top',
      },
    },
  },
  dataLabels: {
    offsetY: -25,
    style: {
      colors: ['#333']
    }
  },
  chart: {
    toolbar: {
      tools: {
        download: false,
        selection: false,
        zoom: false,
        zoomin: false,
        zoomout: false,
      }
    },
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
  },
  series: [{
    name: 'series-1',
    data: [props.weekIncome.monday, props.weekIncome.tuesday, props.weekIncome.wednesday, props.weekIncome.thursday, props.weekIncome.friday, props.weekIncome.saturday, props.weekIncome.sunday]
  }],
}
</script>