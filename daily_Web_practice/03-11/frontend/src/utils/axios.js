const axios = require("axios")

const api = axios.create({
    baseURL: "http://localhost:8000/api/data"
})

export const dataLap = {
    get: () => {
        return api.get("/")
    },
    post: (data) => {
        return api.post("/", data)
    },
    delete: () => {
        return api.delete("/")
    }
}