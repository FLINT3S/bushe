<template>
    <n-config-provider
            :date-locale="dateRuRU"
            :locale="ruRU"
            :theme="appTheme"
            :theme-overrides="overrides"
    >
        <transition mode="out-in" name="fade">
            <component :is="layout">
                <n-dialog-provider>
                    <n-message-provider>
                        <router-view v-slot="{ Component }">
                            <transition mode="out-in" name="fade">
                                <component :is="Component"/>
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
import themeOverridesLight from "@app/style/theme/naive-ui-theme-overrides.json";
import themeOverridesDark from "@app/style/theme/naive-ui-theme-overrides-dark.json";
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

const overrides = computed(() => {
    return root.theme === "light" ? themeOverridesLight : themeOverridesDark
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
