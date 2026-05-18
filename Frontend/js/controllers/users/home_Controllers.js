export class HomeControllers{
    constructor(model){
        this.model = model;
    }
    async getItems(page){
        return await this.model.getItems(page)
    }

}