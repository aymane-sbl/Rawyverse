import { initApi } from "../init_api/api.js";
export async function  fetchData(endpoints){
        let response = await initApi(endpoints);
        return response;
    }
