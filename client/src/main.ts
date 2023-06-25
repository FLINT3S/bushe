import {createApp, Suspense} from 'vue'
import {router} from "@app/providers/router/router";
import {store} from "@app/providers/store/pinia";

import App from '@app/App.vue'
import '@app/style/index.css'

import "reflect-metadata"
import "es6-shim"

declare global {
    interface Window { ymaps: any; }
}

createApp(App)
    .use(store)
    .use(router)
    .mount('#app')

