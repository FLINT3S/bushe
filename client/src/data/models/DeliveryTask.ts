import {DeliveryTaskStatus} from "@data/models/DeliveryTaskStatus";
import {Order} from "@data/models/Order";
import { Type } from "class-transformer";
import {User} from "@data/models/User";

export class DeliveryTask {
    id!: number;

    @Type(() => User)
    user!: User;

    @Type(() => DeliveryTaskStatus)
    status!: DeliveryTaskStatus;

    @Type(() => Order)
    orders!: Order[];
}