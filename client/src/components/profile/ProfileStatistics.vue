<template>
    <div class="stats__inner d-flex flex-column">
        <div class="stats-header">статистика</div>
        <div class="stats__widget">
            <StatisticWidget :mode="'заработано'" :values="stats.earned"/>
            <StatisticWidget :mode="'доставлено'" :values="stats.delivered"/>
            <a class="text-decoration-none" href="https://t.me/zerodaayy" target="_blank">
                <n-button block class="mb-3" secondary type="primary">
                    Связь с менеджером
                </n-button>
            </a>
            <OrderHistoryButton to="/completed">история заказов</OrderHistoryButton>
        </div>
    </div>
</template>

<script lang="ts" setup>
import StatisticWidget from "@components/profile/StatisticWidget.vue";
import OrderHistoryButton from "@shared/components/OrderHistoryButton.vue";

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
</script>

<style scoped>
.stats-header {
    font-size: 16px;
    line-height: 100%;
    margin-top: 29px;
    margin-bottom: 15px;
}
</style>