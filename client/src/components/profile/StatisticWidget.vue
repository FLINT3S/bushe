<template>
  <div class="stats-widget__inner">
    <div class="widget-info">
      <div class="stats-widget-header">заработано <span>{{}}</span></div>
    </div>
    <div class="widget-btn">
      <SettingsIcon></SettingsIcon>
    </div>
  </div>
</template>

<script lang="ts">
import SettingsIcon from "@shared/ui/icon/SettingsIcon.vue";

export default {
  components: {SettingsIcon}
}
</script>

<style scoped>
.stats-widget__inner {
  background-color: #f3f4f4;
  padding: 25px 29px;
}
</style>