<template>
  <div class="profile-card__inner d-flex">
    <div class="profile-card d-flex flex-grow-1 flex-column align-items-center" >
      <div class="profile-card__image">
        <img
            class="profile-card-img"
            src="@/shared/assets/img/user.png"
            alt="Фото профиля"
        />
      </div>
      <div class="profile-card__info">{{ `${user.name} ${user.surname}` }}</div>

    </div>
    <div class="profile-card__buttons d-flex flex-column">
      <edit-icon class="profile-card-btn"/>
      <settings-icon />
    </div>
  </div>
</template>

<script lang="ts" setup>
import EditIcon from "@shared/ui/icon/EditIcon.vue";
import SettingsIcon from "@shared/ui/icon/SettingsIcon.vue";
import {useUserStore} from "@shared/model/store/useUserStore";

const userStore = useUserStore()
const user = ref(userStore.currentUser)

// TODO: computed() из стора
// const fullName = computed((user) => {
//   return user.firstName + user.surname
// })
</script>
<style lang="scss" scoped>
.profile-card__inner {
  margin-top: 10px;
}
.profile-card-img {
  height: 108px;
  width: 108px;
}
.profile-card {
  font-size: 24px;
}
.profile-card-btn {
  margin-bottom: 2px;
}
.card-info {
  font-size: 24px;
  height: content-box;
}
</style>