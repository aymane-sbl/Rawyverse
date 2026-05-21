import { initApi } from "../../../init_api/api.js";

export class BooksModels{

    async getBooks(){
        let response = await initApi("/api/v1/items/books")
        return response
    }
}