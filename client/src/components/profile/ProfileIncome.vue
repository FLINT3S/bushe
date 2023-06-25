<template>
    <div class="income__inner d-flex flex-column">
        <div class="income-header">доход</div>
        <div class="income__dashboard">
            <div class="income-dashboard__widget">
                <IncomeDashboard :week-income="stats.income"/>
            </div>
            <div class="income-dashboard__average">
                в среднем за неделю {{ averageIncome }}
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import IncomeDashboard from "@/components/profile/IncomeDashboard.vue";

interface Props {
    stats: {
        delivered: {
            perDay: number,
            perMonth: number
        },
        earned: {
            perDay: number,
            perMonth: number
        },
        income: {
            monday: number,
            tuesday: number,
            wednesday: number,
            thursday: number,
            friday: number,
            saturday: number,
            sunday: number
        }
    }
}

const props = defineProps<Props>()
const averageIncome = computed(() => {
    let weekIncome: number = 0;
    let key: keyof typeof props.stats.income;
    for (key in props.stats?.income) {
        weekIncome += props.stats?.income?.[key];
    }
    const avg = weekIncome / 7
    return avg.toFixed(2)
})
</script>

<style scoped>
.income-header {
    margin-top: 35px;
}

.income-dashboard__average {
    font-size: 16px;
    text-align: center;
}
</style>