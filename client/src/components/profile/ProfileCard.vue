<template>
  <n-card class="profile-card__inner">
    <div class="profile-card d-flex align-items-center" >
      <div class="profile-card__image">
        <img
            class="profile-card-img"
            src="@/shared/assets/img/user.jpeg"
            alt="Фото профиля"
        />
      </div>

      <div class="profile-card__info d-flex flex-grow-1 justify-content-center align-items-start flex-column ">
        <div class="profile-card-info__item">{{ user.userName }}</div>
        <div class="profile-card-info__item">{{ user.userSurname }}</div>
        <div class="profile-card-info__rate">
          <rating-icon>{{ user.rating}}</rating-icon>
        </div>
      </div>

    </div>
  </n-card>
</template>

<script lang="ts" setup>
import RatingIcon from "@/components/ui/icons/RatingIcon.vue"

interface Props {
  user: {
    userName: string,
    userSurname: string,
    rating: number
  },
}
const props = defineProps<Props>()
</script>
<style lang="scss" scoped>
.profile-card__inner {
  margin-top: 10px;
}
.profile-card-img {
  height: 155px;
  width: 115px;
  margin-right: 30px;
}
.profile-card {
  font-size: 24px;
}
.profile-card-info__item {
  border-bottom: 1px solid black;
  width: 100%;
}
</style>