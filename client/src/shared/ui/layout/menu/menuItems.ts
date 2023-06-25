import {MenuDividerOption, MenuGroupOption, MenuOption, NIcon} from "naive-ui";
import PlannedIcon from "@shared/ui/icon/PlannedIcon.vue";
import ProcessIcon from "@shared/ui/icon/ProcessIcon.vue";
import ProfileIcon from "@shared/ui/icon/ProfileIcon.vue";
import {Component, VNodeChild} from "vue";
import {RouterLink} from "vue-router";
import ManagerIcon from "@shared/ui/icon/ManagerIcon.vue";
import DeliveryTasksIcon from "@shared/ui/icon/DeliveryTasksIcon.vue";

const renderIcon = (icon: Component) => {
    return (iconSize: string | number | undefined = undefined, color: string = "white") => h(NIcon, {size: iconSize}, {default: () => h(icon, {color})})
}

const renderLabel = (text: string, path: string) => {
    return h(
        RouterLink,
        {
            to: {
                path: path
            }
        },
        {default: () => text}
    )
}

export const menuItems: Array<MenuOption & {path: string, icon: any}> = [
    {
        path: "/planned",
        label: () => renderLabel("запланированные", "/planned"),
        key: "planned",
        icon: renderIcon(PlannedIcon),
        roles: [1, 3]
    },
    {
        path: "/process",
        label: () => renderLabel("в процессе", "/process"),
        key: "process",
        icon: renderIcon(ProcessIcon),
        roles: [1, 3]
    },
    {
        path: "/profile",
        label: () => renderLabel("личный кабинет", "/profile"),
        key: "profile",
        icon: renderIcon(ProfileIcon),
        roles: [1, 3]
    },
    {
        path: "/manageOrders",
        label: () => renderLabel("управление заказами", "/manageOrders"),
        key: "manageOrders",
        icon: renderIcon(ManagerIcon),
        roles: [2, 3]
    },
    {
        path: "/manageDeliveryTasks",
        label: () => renderLabel("задачи на доставку", "/manageDeliveryTasks"),
        key: "manageDeliveryTasks",
        icon: renderIcon(DeliveryTasksIcon),
        roles: [2, 3]
    }
]