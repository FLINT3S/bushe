export class DeliveryTaskStatus {
    id!: number
    name!: "Задача создана" | "Назначено" | "Готовится" | "Ожидает выдачи" | "В доставке" | "Доставлен"
}