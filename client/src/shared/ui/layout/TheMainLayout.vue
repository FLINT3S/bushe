<template>
    <main>
        <n-space vertical>
            <n-layout style="height: 100vh">
                <n-layout-header bordered style="height: 64px; padding: 16px">
                    <div class="d-flex justify-content-between">
                        <n-space>
                            <n-h3>буше доставка</n-h3>
                        </n-space>

                        <n-button @click="onClickThemeChange">
                            тема
                        </n-button>
                    </div>
                </n-layout-header>

                <n-layout
                        :has-sider="windowWidth >= 992"
                        :native-scrollbar="windowWidth >= 992"
                        position="absolute"
                        style="top: 64px; bottom: 0"
                >
                    <n-layout-sider
                            v-if="windowWidth >= 992"
                            :collapsed-width="64"
                            :width="240"
                            bordered
                            class="sider h-100"
                            collapse-mode="width"
                            content-style="display: flex; flex-direction: column; height: 100%"
                            inverted
                            show-trigger
                            @updateCollapsed="onUpdateCollapsed"
                    >
                        <n-menu
                                :collapsed-icon-size="22"
                                :collapsed-width="64"
                                :options="menuItemsFiltered"
                                :value="selectedMenuItem"
                                inverted
                        />

                        <div class="mt-auto p-3">
                            <n-collapse-transition :show="!isSiderCollapsed">
                                <n-button block type="primary" @click="onClickLogout">
                                    Выйти

                                    <template #icon>
                                        <n-icon :component="LogoutIcon"/>
                                    </template>
                                </n-button>
                            </n-collapse-transition>
                        </div>
                    </n-layout-sider>

                    <n-layout-content
                            ref="contentRef"
                            :native-scrollbar="false"
                            content-style="padding: 24px 24px 0 24px;"
                    >
                        <n-layout
                                :content-style="windowWidth < 992 ? 'padding-bottom: 86px' : 'padding-bottom: 32px'"
                                :native-scrollbar="false"
                        >
                            <slot></slot>
                        </n-layout>
                    </n-layout-content>
                </n-layout>

                <n-layout-footer v-if="windowWidth < 992" class="bottom-nav" position="fixed">
                    <div class="px-3 py-3 d-flex justify-content-around">
                        <router-link v-for="menuItem in menuItemsFiltered" :to="menuItem.path">
                            <component :is="menuItem.icon(24, route.path === menuItem.path ? 'var(--orange-accent)' : 'white')"/>
                        </router-link>
                    </div>
                </n-layout-footer>
            </n-layout>
        </n-space>
    </main>
</template>

<script lang="ts" setup>
import {useRootStore} from "@shared/model/store/useRootStore";
import {menuItems} from "@shared/ui/layout/menu/menuItems";
import LogoutIcon from "@shared/ui/icon/LogoutIcon.vue";
import {useUserStore} from "@shared/model/store/useUserStore";
import {storeToRefs} from "pinia";

const route = useRoute()
const router = useRouter()
const root = useRootStore()
const userStore = useUserStore()
const {currentUser} = storeToRefs(userStore)

const windowWidth = ref(0)

const menuItemsFiltered = computed(() => {
    return menuItems.filter((m: any) => m?.roles?.includes(currentUser.value?.role))
})

const onClickThemeChange = () => {
    if (root.theme === 'dark') {
        root.setTheme('light')
    } else {
        root.setTheme('dark')
    }
}

const selectedMenuItem = computed(() => {
    return route.meta.menuItemKey
})

const isSiderCollapsed = ref(false)

const onClickLogout = () => {
    router.push("/logout")
}

const onUpdateCollapsed = (v: boolean) => {
    isSiderCollapsed.value = v
}

const onWindowResize = () => {
    windowWidth.value = window.innerWidth
}

onMounted(() => {
    nextTick(() => {
        windowWidth.value = window.innerWidth
        window.addEventListener("resize", onWindowResize)
    })
})

onBeforeUnmount(() => {
    window.removeEventListener("resize", onWindowResize)
})
</script>

<style>
aside.sider {
    background-color: black;
}

.layout-content {
    height: 80vh;
}

.bottom-nav {
    z-index: 100;
    position: fixed;
    bottom: 0;
    width: 100%;
    background: #000;
    color: white;
}

#app > div > main > div > div > div > div > div.n-layout.n-layout--absolute-positioned > div > div.n-scrollbar-container > div > div > div > div.n-scrollbar-container > div {
    padding: 12px 12px 0 12px!important;

    @media screen and (min-width: 768px) {
        padding: 24px 24px 0 24px;
    }
}
</style>