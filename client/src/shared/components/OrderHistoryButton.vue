<template>
  <router-link to="/completed" class="btn-link">
    <div class="btn__inner d-flex">
      <div class="btn-text flex-grow-1">
        <slot></slot>
      </div>
      <div class="btn-icon d-flex align-items-center">
        <LongRightArrow />
      </div>
    </div>
  </router-link>
</template>

<script lang="ts" setup>
import LongRightArrow from "@shared/ui/icon/LongRightArrow.vue";
const router = useRouter();
</script>

<style scoped>
.btn__inner {
  background-color: #f3f4f4;
  padding: 12px 29px;
}
.btn__inner:hover{ background-color: #ebebeb;}
.btn__inner:active{ background-color: #e8e8e8;}

.btn-text {
  font-size: 16px;
}
.btn-link {
  text-decoration: none;
  color:inherit;
}
</style>