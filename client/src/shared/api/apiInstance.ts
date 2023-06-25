import axios from "axios";

export const apiInstance = axios.create({
    baseURL: !import.meta.env.DEV ? "https://bushe.flint3s.ru/api" : "http://localhost:3000/api",
    headers: {
        "Content-Type": "application/json"
    }
})