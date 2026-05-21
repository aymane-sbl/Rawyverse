import { initApi } from "../../../init_api/api.js";

export class NovelsModels{

    async getNovels(){
        let response = await initApi("/api/v1/items/novels")
        return response
    }
}