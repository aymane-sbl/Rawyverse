import { initApi } from "../../api.js";

export class NovelsModels{

    async getNovels(){
        let response = await initApi("/api/v1/items/novels")
        return response
    }
}