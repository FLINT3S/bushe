import {defineStore} from "pinia";
import {CurrentUser} from "@data/models/CurrentUser";

export const useUserStore = defineStore("user", {
    state() {
        return {
            currentUser: null as CurrentUser | null
        }
    }
})