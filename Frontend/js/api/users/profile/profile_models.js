import {fetchData} from "../../../utils/fetchj_data.js"

export class ProfileModels{

    async getCurrentUser(){
        const endpoints = "/api/v1/me";
        let response = await fetchData(endpoints);
        return response
    }
}