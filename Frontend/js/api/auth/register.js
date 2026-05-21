import { initApi } from "../../init_api/api.js";
export class RegisterModels{
    async register(userName,email,password){
    let endpoints = "/api/v1/register";
    let data = {
            "userName":userName,
            "email":email,
            "password":password
        };
    let options = {
        method:"POST",
        credentials : "include",
        headers:{
            "Content-Type": "application/json"
        },
        body : JSON.stringify(data)
    };

    let response = await initApi(endpoints,options);
    return response
    
}
}