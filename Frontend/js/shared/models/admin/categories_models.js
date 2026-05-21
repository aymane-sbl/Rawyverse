import { initApi } from "../../../init_api/api.js";

export class CategorieModels{
    async addCategories(name){
        let endpoints = "/api/v1/admin/categories/";
        let data = {
            "CategoryName" :  name
        }
        let options = {

            method : "POST",
            headers:{
                "content-type" : "application/json",
            },
            credentials : "include",
            body : JSON.stringify(data)

        };

        let response = await initApi(endpoints,options)
        return response
    }

    async deleteCategories(name){
        let endpoints = "/api/v1/admin/categories/";
        let data = {
            "CategoryName" :  name
        }
        let options = {

            method : "DELETE",
            headers:{
                "content-type" : "application/json",
            },
            credentials : "include",
            body : JSON.stringify(data)

        };

        let response = await initApi(endpoints,options)
        return response
    }
}