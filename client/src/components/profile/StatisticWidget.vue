<template>
  <div class="stats-widget__inner d-flex">
    <div class="widget-info d-flex flex-grow-1 flex-column align-self-start">
      <div class="stats-widget-header align-self-start">{{mode}} за <span>{{statisticMode}}</span></div>

      <div class="stats-widget-value d-flex justify-content-center align-items-center">
        <div class="stats-widget-value__number">{{statisticMode === 'день'? values.perDay : values.perMonth}}</div>
        <div class="stats-widget-value__number currency"
             v-if="mode === 'заработано'"
        >₽</div>
        <div class="stats-widget-value__icon box"
             v-if="mode === 'доставлено'">
          <BoxIcon class="d-flex align-self-end"/>
        </div>
      </div>
    </div>
    <div class="widget-btn d-flex align-self-start justify-content-start">
      <n-popselect v-model:value="statisticMode" :options="statisticModeOptions">
        <n-button text style="font-size: 20px">
          <n-icon>
            <svg width="21" height="17" viewBox="0 0 21 17" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M5.83333 6.79986C6.60927 6.79974 7.36318 6.54921 7.97663 6.08765C8.59009 5.62609 9.02832 4.97965 9.2225 4.24986H21V2.54986H9.2225C9.02789 1.8205 8.58946 1.17455 7.97605 0.71343C7.36264 0.252305 6.60896 0.00210571 5.83333 0.00210571C5.0577 0.00210571 4.30403 0.252305 3.69061 0.71343C3.0772 1.17455 2.63878 1.8205 2.44417 2.54986H0V4.24986H2.44417C2.63834 4.97965 3.07658 5.62609 3.69003 6.08765C4.30349 6.54921 5.0574 6.79974 5.83333 6.79986ZM5.83333 5.09986C6.29746 5.09986 6.74258 4.92076 7.07077 4.60195C7.39896 4.28313 7.58333 3.85073 7.58333 3.39986C7.58333 2.949 7.39896 2.51659 7.07077 2.19778C6.74258 1.87897 6.29746 1.69986 5.83333 1.69986C5.3692 1.69986 4.92409 1.87897 4.5959 2.19778C4.26771 2.51659 4.08333 2.949 4.08333 3.39986C4.08333 3.85073 4.26771 4.28313 4.5959 4.60195C4.92409 4.92076 5.3692 5.09986 5.83333 5.09986ZM11.7775 13.3165H0V11.6165H11.7775C11.9721 10.8872 12.4105 10.2412 13.0239 9.7801C13.6374 9.31897 14.391 9.06877 15.1667 9.06877C15.9423 9.06877 16.696 9.31897 17.3094 9.7801C17.9228 10.2412 18.3612 10.8872 18.5558 11.6165H21V13.3165H18.5558C18.3612 14.0459 17.9228 14.6918 17.3094 15.153C16.696 15.6141 15.9423 15.8643 15.1667 15.8643C14.391 15.8643 13.6374 15.6141 13.0239 15.153C12.4105 14.6918 11.9721 14.0459 11.7775 13.3165ZM16.9167 12.4665C16.9167 12.9174 16.7323 13.3498 16.4041 13.6686C16.0759 13.9874 15.6308 14.1665 15.1667 14.1665C14.7025 14.1665 14.2574 13.9874 13.9292 13.6686C13.601 13.3498 13.4167 12.9174 13.4167 12.4665C13.4167 12.0157 13.601 11.5833 13.9292 11.2644C14.2574 10.9456 14.7025 10.7665 15.1667 10.7665C15.6308 10.7665 16.0759 10.9456 16.4041 11.2644C16.7323 11.5833 16.9167 12.0157 16.9167 12.4665Z" fill="#0E0E0E"/>
            </svg>
          </n-icon>
        </n-button>
      </n-popselect>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {Ref} from "vue";
import {StatisticPeriodMode} from "@data/types/statisticPeriodMode";
import {StatisticActionMode} from "@data/types/statisticActionMode";
import BoxIcon from "@shared/ui/icon/BoxIcon.vue";

interface Props {
  mode: StatisticActionMode,
  values: {
    perDay: number,
    perMonth: number
  }
}
const statisticMode: Ref<StatisticPeriodMode> = ref('день');
const statisticModeOptions = [
  {
    label: 'день',
    value: 'день'
  },
  {
    label: 'месяц',
    value: 'месяц'
  }
]

const props = defineProps<Props>()
</script>

<style scoped>
.stats-widget__inner {
  background-color: #f3f4f4;
  padding: 25px 29px;
  margin-bottom: 15px;
}
.stats-widget-header {
  line-height: 100%;
  font-size: 16px;
  margin-bottom: 12px;
}
.stats-widget-header span {
  color: #B9BABA;
}
.stats-widget-value__number {
  font-size: 24px;
  line-height: 100%;
}
.stats-widget-value__icon.box, .stats-widget-value__number.currency {
  margin-left: 5px;
}

</style>