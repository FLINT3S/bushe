<template>
    <div class="container h-fluid d-flex">
        <div class="login-inner-container my-auto d-block mx-auto">
            <n-card class="w-100 login-card">
                <div class="login-card__picture w-100">
                    <img alt="" class="d-none d-md-block w-100 h-100" src="@shared/assets/img/login-cover.png">
                    <img alt="" class="d-block d-md-none w-100 h-100" src="@shared/assets/img/login-cover-sm.png">
                </div>
                <div class="w-100 px-4 py-4 py-md-5 text-center">
                    <div class="d-flex">
                        <n-h2 class="text-start mx-auto">
                            буше
                            <br>
                            доставка
                        </n-h2>
                    </div>

                    <n-form class="mt-5">
                        <n-form-item label="Логин">
                            <n-input v-model:value="loginData.login" placeholder="Логин"/>
                        </n-form-item>

                        <n-form-item label="Пароль">
                            <n-input v-model:value="loginData.password" placeholder="Пароль" type="password"/>
                        </n-form-item>

                        <n-button block class="mt-4" type="primary" @click="onClickSubmitLogin">
                            Войти
                        </n-button>

                        <n-collapse-transition :show="loginError !== ''">
                            <n-alert v-if="loginError" class="mt-4" closable title="Ошибка логина" type="error"
                                     @close="loginError = ''">
                                {{ loginError }}
                            </n-alert>
                        </n-collapse-transition>
                    </n-form>
                </div>
            </n-card>
        </div>
    </div>
</template>

<script lang="ts" setup>

import {apiInstance} from "@shared/api/apiInstance";
import {LocalStorageKeys} from "@shared/model/LocalStorageKeys";

const router = useRouter()

const loginData = reactive({
    login: "",
    password: ""
})

const loginError = ref("")

const onClickSubmitLogin = () => {
    apiInstance.post("/auth/login", loginData)
        .then((response) => {
            router.replace("/")
            localStorage.setItem(LocalStorageKeys.ACCESS_TOKEN, response.data.accessToken)
        })
        .catch((reason) => {
            loginError.value = "Проверьте логин и пароль"
        })
}
</script>

<style lang="scss" scoped>
.h-fluid {
  height: 100vh;
}

.login-inner-container {
  width: 100%;

  @media screen and (min-width: 992px) {
    width: 768px;
  }
}
</style>

<style lang="scss">
.login-card {
  .n-card__content {
    display: flex;
    padding: 0 !important;

    .login-card__picture {
      img {
        object-fit: cover;
        object-position: center center;
      }
    }

    @media screen and (max-width: 992px) {
      flex-direction: column;

      .login-card__picture {
        min-height: 25vh;
        max-height: 30vh;
        overflow: hidden;

        img {
          object-fit: cover;
          object-position: center center;
        }
      }
    }
  }
}
</style>