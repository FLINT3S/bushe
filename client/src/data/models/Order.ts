import {OrderStatus} from "@data/models/OrderStatus";
import {Type} from "class-transformer";

export class Order {
    id!: number;

    @Type(() => Date)
    deadline!: Date;

    address!: string;

    weight!: number;

    @Type(() => OrderStatus)
    status!: OrderStatus;

    get deadlineFormat() {
        return `${String(this.deadline.getHours()).padStart(2, '0')}:${String(this.deadline.getMinutes()).padStart(2, '0')}`;
    }

    get isCompleted() {
        return this.status.name === "Заказ доставлен"
    }
}