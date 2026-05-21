import { initApi } from "../../../init_api/api.js";

export class SearchModels {
    async search(title){
        let endpoints = `/api/v1/items/search?title=${title}`;
        let response = await initApi(endpoints);
        return response
        
    }
}