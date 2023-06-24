<template>
    <svg class="planned-icon" fill="none" viewBox="0 0 20 26" xmlns="http://www.w3.org/2000/svg">
        <path d="M6.25 4.25H3.75C3.08696 4.25 2.45107 4.51339 1.98223 4.98223C1.51339 5.45107 1.25 6.08696 1.25 6.75V21.75C1.25 22.413 1.51339 23.0489 1.98223 23.5178C2.45107 23.9866 3.08696 24.25 3.75 24.25H16.25C16.913 24.25 17.5489 23.9866 18.0178 23.5178C18.4866 23.0489 18.75 22.413 18.75 21.75V6.75C18.75 6.08696 18.4866 5.45107 18.0178 4.98223C17.5489 4.51339 16.913 4.25 16.25 4.25H13.75"
              :stroke="color" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
        <path d="M11.25 1.75H8.75C7.36929 1.75 6.25 2.86929 6.25 4.25C6.25 5.63071 7.36929 6.75 8.75 6.75H11.25C12.6307 6.75 13.75 5.63071 13.75 4.25C13.75 2.86929 12.6307 1.75 11.25 1.75Z"
              :stroke="color" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
        <path d="M6.25 13H6.2625" :stroke="color" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
        <path d="M11.25 13H13.75" :stroke="color" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
        <path d="M6.25 18H6.2625" :stroke="color" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
        <path d="M11.25 18H13.75" :stroke="color" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
    </svg>
</template>

<script lang="ts" setup>
interface Props {
    color?: string
}

const props = withDefaults(defineProps<Props>(), {
    color: "white"
})
</script>
