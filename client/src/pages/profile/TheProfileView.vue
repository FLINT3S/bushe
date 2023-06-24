<template>
  <div class="container">
    <div class="col">
      <div class="profile-header"> личный кабинет</div>
      <div class="profile-section row-cols-1">
        <profile-card />
      </div>

      <div class="profile-section row-cols-1">
        <ProfileStatistics />
      </div>

      <div class="profile-section row-cols-1">
        dashboard
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import ProfileCard from "@/components/profile/ProfileCard.vue"
import ProfileStatistics from "@components/profile/ProfileStatistics.vue";
</script>

<style lang="scss" scoped>
.profile-header{
  font-size: 32px;
  width: 100%;
  line-height: 100%;

}
</style>