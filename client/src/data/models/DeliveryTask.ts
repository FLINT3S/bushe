import {DeliveryTaskStatus} from "@data/models/DeliveryTaskStatus";
import {Order} from "@data/models/Order";
import { Type } from "class-transformer";

export class DeliveryTask {
    id!: number;

    user!: string;

    @Type(() => DeliveryTaskStatus)
    status!: DeliveryTaskStatus;

    @Type(() => Order)
    orders!: Order[];
}