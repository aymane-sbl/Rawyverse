import {initApi} from "../../api.js"
export class DetailsModels{
     // get items by id
    async getItemsById(id){
        let endpoints = `/api/v1/items/details/${id}`;
        let options = {methode : "GET",};
        let response = await initApi(endpoints,options);
        return response
    }
}