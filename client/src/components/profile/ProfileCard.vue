<template>
  <div class="profile-card__inner">
    <div class="profile-card__buttons d-flex flex-column">

    </div>
    <div class="profile-card d-flex flex-grow flex-column align-items-center" >
      <div class="profile-card__image">
        <img
            class="profile-card-img"
            src="@/shared/assets/img/user.png"
            alt="Фото профиля"
        />
      </div>

      <div class="profile-card__info">{{ `${user.firstName} ${user.surname}` }}</div>
    </div>
  </div>
</template>

<script lang="ts" setup>
// // TODO: user подтянуть из стора
const user = ref({
  id: 1,
  firstName: 'Иван',
  surname: 'Иванов'
})
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
  margin-bottom: 15px;
}
.profile-card {
  font-size: 24px;
}
</style>