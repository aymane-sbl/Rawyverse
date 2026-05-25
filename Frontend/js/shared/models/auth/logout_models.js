import {initApi} from "../../../init_api/api.js"
export class LogoutModels{
    async logout(){
        const endpoints = "/api/v1/logout";
        let options = {
            method  : "POST",
            credentials : "include",
            headers : {
                "content-type" : "application/json"
            }
        }
        let response =await  initApi(endpoints,options);
        return response

    }
}