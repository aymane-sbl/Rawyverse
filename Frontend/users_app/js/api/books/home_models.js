import {initApi} from "../api.js"
export class HomeModels{
    async getItems(){
        const endpoints = "/api/v1/items/?page=1&limit=20";
        let options = {methode : "GET"};
        let response = await initApi(endpoints,options);
        return response

    }
     // get items by id
    async getItemsById(id){
        let endpoints = `/api/v1/items/details/${id}`;
        let options = {methode : "GET",};
        let response = await initApi(endpoints,options);
        return response
    }
}