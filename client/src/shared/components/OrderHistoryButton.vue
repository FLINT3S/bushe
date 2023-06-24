<template>
  <div class="btn__inner d-flex align-self-center">
    <div class="btn-text flex-grow-1">
      <slot></slot>
    </div>
    <div class="btn-icon d-flex align-items-center">
      <LongRightArrow />
    </div>
  </div>
</template>

<script lang="ts" setup>
import LongRightArrow from "@shared/ui/icon/LongRightArrow.vue";
</script>

<style scoped>
.btn__inner {
  background-color: #f3f4f4;
  padding: 12px 29px;
}
.btn-text {
  font-size: 16px;
}
</style>