<template>
  <div class="container">
    <div class="col">
      <div class="profile-header"> личный кабинет</div>
      <div class="profile-section row-cols-1">
        <profile-card />
      </div>

      <div class="profile-section row-cols-1">
        <ProfileStatBtns />
      </div>

      <div class="profile-section row-cols-1">
        dashboard
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import ProfileCard from "@/components/profile/ProfileCard.vue"
import ProfileStatBtns from "@components/profile/ProfileStatBtns.vue";
</script>

<style lang="scss" scoped>
.container {
  padding: 0 24px;
}
.profile-header{
  font-size: 32px;
  margin-top:70px;
  width: 100%;

}
</style>