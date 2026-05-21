import {initApi} from "../../init_api/api.js"
export class HomeModels{
    async getItems(page){
        const endpoints = `/api/v1/items/?page=${page}&limit=20`;
        let response = await initApi(endpoints);
        return response

    }

}

