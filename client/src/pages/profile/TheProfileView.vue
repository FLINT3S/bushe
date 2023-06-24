<template>
  <div class="container">
    <div class="col">
      <div class="profile-section row-cols-1">
        <profile-card :user="user" />
      </div>

      <div class="profile-section row-cols-1">
        <profile-stat-btns />
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

const user = {
  userName: 'Иван',
  userSurname: 'Иванов',
  rating: 4.8
}
</script>