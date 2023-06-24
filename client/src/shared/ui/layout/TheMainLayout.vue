<template>
    <main>
        <n-space vertical>
            <n-layout style="height: 100vh">
                <n-layout-header bordered style="height: 64px; padding: 16px">
                    <n-space>
                        <n-h3>буше доставка</n-h3>
                    </n-space>
                </n-layout-header>

                <n-layout :has-sider="windowWidth >= 992" position="absolute" style="top: 64px; bottom: 0">
                    <n-layout-sider
                            v-if="windowWidth >= 992"
                            :collapsed-width="64"
                            :width="240"
                            bordered
                            class="sider"
                            collapse-mode="width"
                            inverted
                            show-trigger
                    >
                        <n-menu
                                :collapsed-icon-size="22"
                                :collapsed-width="64"
                                :options="menuItems"
                                :value="selectedMenuItem"
                                inverted
                        />
                    </n-layout-sider>

                    <n-layout-content
                            ref="contentRef"
                            :native-scrollbar="false"
                            content-style="padding: 24px 24px 0 24px;"
                    >
                        <div>
                            <slot></slot>
                        </div>
                    </n-layout-content>
                </n-layout>

                <n-layout-footer position="fixed" class="bottom-nav" v-if="windowWidth < 992">
                    <div class="px-3 py-3 d-flex justify-content-around">
                        <router-link :to="menuItem.path" v-for="menuItem in menuItems">
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

const route = useRoute()
const root = useRootStore()

const windowWidth = ref(0)

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
</style>