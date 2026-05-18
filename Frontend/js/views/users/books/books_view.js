import { get_specific_items_category_views } from "../../../shared/view/get_specific_items_category_views.js";
export class BooksView{
    constructor (controller){
        this.controller = controller;
    }
    async getBooks(){
        let controller = await this.controller.getBooks()
        get_specific_items_category_views(controller)
    }
}
