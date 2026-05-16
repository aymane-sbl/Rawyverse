export class HomeControllers{
    constructor(model){
        this.model = model;
    }
    async getItems(){
        return await this.model.getItems()
    }
    async getItemsById(id){
        return await this.model.getItemsById(id)
    }
}