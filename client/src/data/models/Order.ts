import {OrderStatus} from "@data/models/OrderStatus";
import {Type} from "class-transformer";

export class Order {
    id!: number;

    @Type(() => Date)
    deadline!: Date;

    address!: string;

    restaurant_address!: string;

    weight!: number;

    @Type(() => OrderStatus)
    status!: OrderStatus;

    status_id?: number
    
    get deadlineFormat() {
        return `${String(this.deadline.getHours()).padStart(2, '0')}:${String(this.deadline.getMinutes()).padStart(2, '0')}`;
    }

    get isCompleted() {
        return this.status_id === 4
    }
}