import {initApi} from "../api.js"
export class HomeModels{
    async getItems(page){
        const endpoints = `/api/v1/items/?page=${page}&limit=20`;
        let options = {methode : "GET"};
        let response = await initApi(endpoints,options);
        return response

    }

}

