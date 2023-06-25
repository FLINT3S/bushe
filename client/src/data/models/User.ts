export class User {
    id!: number
    login!: string
    name!: string
    surname!: string

    get fullName() {
        return `${this.name} ${this.surname}`
    }
}