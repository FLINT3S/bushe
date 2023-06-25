import axios from "axios";

export const apiInstance = axios.create({
    // baseURL: "https://bushe.flint3s.ru/api",
    baseURL: "http://localhost:3000/api",
    headers: {
        "Content-Type": "application/json"
    }
})