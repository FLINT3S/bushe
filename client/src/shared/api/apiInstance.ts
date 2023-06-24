import axios from "axios";

export const apiInstance = axios.create({
    baseURL: "https://bushe.flint3s.ru/api",
    headers: {
        "Content-Type": "application/json"
    }
})