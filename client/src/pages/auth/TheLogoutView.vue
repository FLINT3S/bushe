<template>

</template>

<script lang="ts" setup>
import {LocalStorageKeys} from "@shared/model/LocalStorageKeys";

const router = useRouter()

onBeforeMount(() => {
    localStorage.setItem(LocalStorageKeys.ACCESS_TOKEN, "")
    window.location.reload()
})

</script>

<style scoped>

</style>