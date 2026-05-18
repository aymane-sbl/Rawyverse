import {initApi} from "../api.js"
export class LoginModels{
    async login(email,password){
        let endpoints = "/api/v1/login"
        let data = {
            "email":email,
            "password":password
        };
        let options = {
            method :"POST",
            headers : {"content-type":"application/json"},
            body : JSON.stringify(data)
        };
        let response = await initApi(endpoints,options);
        return  response
    }
}