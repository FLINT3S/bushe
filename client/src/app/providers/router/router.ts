import {createRouter, createWebHashHistory} from "vue-router";
import {routes} from "./routes";
import {LocalStorageKeys} from "@shared/model/LocalStorageKeys";

export const router = createRouter({
    history: createWebHashHistory(),
    routes
})

router.beforeEach((to, from) => {
    if (to.path !== "/login") {
        if (!localStorage.getItem(LocalStorageKeys.ACCESS_TOKEN)) {
            return {path: "/login"}
        }
    }
})