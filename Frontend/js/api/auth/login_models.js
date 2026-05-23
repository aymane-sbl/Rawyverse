import {initApi} from "../../init_api/api.js"
export class LoginModels{
    async login(email,password){
        let endpoints = "/api/v1/login/"
        let data = {
            "email":email,
            "password":password
        };
        let options = {
            method :"POST",
            credentials : "include",
            headers : {"Content-Type":"application/json"},
            body : JSON.stringify(data)
        };
        let response = await initApi(endpoints,options);
        return  response
    }
    async loginWithGoogle(token){
        const endpoints = "/api/v1/google-login";
        let data = {
            "token":token
        }
        let options = {
            method : "POST",
            credentials : "include",
            headers : {
                "Content-type":"application/json",
            },
            body : JSON.stringify(data)
        }

        let response = initApi(endpoints,options);
        return response;
    }
}