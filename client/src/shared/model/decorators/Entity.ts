import {API} from "@/shared/data/models/common/api/API";

type EntityOptions = {
    disableApi?: boolean
}

export const Entity = (options: EntityOptions = {disableApi: false}) => {
    return (target: any) => {
        if (!options.disableApi) {
            target.$api = new API(new target().api?.path || `/${target.name.toLowerCase()}`)
        } else {
            target.$api = null
        }
    }
}
