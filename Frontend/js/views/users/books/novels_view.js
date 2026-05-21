import { get_specific_items_category_views } from "../../../shared/view/get_specific_items_category_views.js";
export class NovelsView{
    constructor (controller){
        this.controller = controller;
    }
    async getNovels(){
        let controller = await this.controller.getNovels()
        get_specific_items_category_views(controller)
    }
}

