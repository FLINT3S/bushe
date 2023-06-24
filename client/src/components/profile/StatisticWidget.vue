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
      <WidgetSettingsIcon />
    </div>
  </div>
</template>

<script lang="ts" setup>
import WidgetSettingsIcon from "@shared/ui/icon/WidgetSettingsIcon.vue";
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