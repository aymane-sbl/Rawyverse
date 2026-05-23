import {initApi} from "../../../init_api/api.js"
import { fetchData } from "../../../utils/fetchj_data.js";
export class ItemsModels{
    async addItems(form){
        const endponits = "/api/v1/admin/items/";
        let options = {
            method : "POST",
            credentials : "include",
            body:form
        }
        let response = await initApi(endponits,options)
        return response
    }
    async deleteItems(title){
        const endpoints = "/api/v1/admin/items/";

        let data = {
            "title":title
        }

        let options = {
            method : "DELETE",
            credentials : "include",
            headers:{
                "accept":"application/json",
                "Content-Type": "application/json"
            },
            body : JSON.stringify(data)
        }

        let response = await initApi(endpoints,options);
        return response
    }
    // get total items 
    async totalItems(){
        let endpoints = "/api/v1/admin/items/length-table";
        return await fetchData(endpoints);
    }
     // total books
    async totalBooks(){
        const endpoints = "/api/v1/admin/items/length-books";
        return await fetchData(endpoints);
    }
     // total books
    async totalNovels(){
        const endpoints = "/api/v1/admin/items/length-novels";
        return await fetchData(endpoints);
    }
}