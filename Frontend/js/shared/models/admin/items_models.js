import {initApi} from "../../../init_api/api.js"
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
}