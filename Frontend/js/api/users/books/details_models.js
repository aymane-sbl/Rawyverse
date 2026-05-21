import {initApi} from "../../../init_api/api.js"
export class DetailsModels{
     // get items by id
    async getItemsById(id){
        let endpoints = `/api/v1/items/details/${id}`;
        let response = await initApi(endpoints);
        return response
    }
}