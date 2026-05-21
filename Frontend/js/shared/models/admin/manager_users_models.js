import {initApi} from "../../../init_api/api.js"
export class ManagerUsersModels{
    async deleteUsers(email){
        const endpoints = "/api/v1/admin/manager-users/";
        let data = {
            "email":email
        }
        let options = {
            method : "DELETE",
            credentials : "include",
            headers : {
                "accept": "application/json",
                "content-type":"application/json"
            },
            body : JSON.stringify(data)
        }
        let response = await initApi(endpoints,options);
        return response


    }
}