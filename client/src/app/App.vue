<template>
    <n-config-provider
            :date-locale="dateRuRU"
            :locale="ruRU"
            :theme="appTheme"
            :theme-overrides="themeOverrides"
    >
        <transition mode="out-in" name="fade">
            <component :is="layout">
                <n-dialog-provider>
                    <n-message-provider>
                        <router-view v-slot="{ Component }">
                            <transition mode="out-in" name="fade">
                                <keep-alive>
                                    <component :is="Component"/>
                                </keep-alive>
                            </transition>
                        </router-view>
                    </n-message-provider>
                </n-dialog-provider>
            </component>
        </transition>
    </n-config-provider>
</template>

<script lang="ts" setup>
import {type Component, computed} from "vue";
import {useRoute} from "vue-router";
import {darkTheme, dateRuRU, lightTheme, ruRU} from "naive-ui";
import {useRootStore} from "@shared/model/store/useRootStore";
import themeOverrides from "@app/style/theme/naive-ui-theme-overrides.json";
import {useUserStore} from "@shared/model/store/useUserStore";
import {storeToRefs} from "pinia";
import {apiInstance} from "@shared/api/apiInstance";
import {LocalStorageKeys} from "@shared/model/LocalStorageKeys";
import {plainToInstance} from "class-transformer";
import {CurrentUser} from "@data/models/CurrentUser";

const route = useRoute()
const router = useRouter()
const root = useRootStore()
const userStore = useUserStore()

const {currentUser} = storeToRefs(userStore)

root.initTheme()

const layout = computed(() => {
    return route.meta?.layout as Component || null
})

const appTheme = computed(() => {
    return root.theme === 'light' ? lightTheme : darkTheme
})

onMounted(() => {
    apiInstance.post("/auth/check", {accessToken: localStorage.getItem(LocalStorageKeys.ACCESS_TOKEN)})
        .then(response => {
            currentUser.value = plainToInstance(CurrentUser, response.data)
        })
        .catch(() => {
            localStorage.setItem(LocalStorageKeys.ACCESS_TOKEN, "")
            router.replace("/login")
        })
})
</script>

<style>
</style>
