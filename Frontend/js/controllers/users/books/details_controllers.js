export class DetailsControllers{
    constructor(model){
        this.model = model;
    }
    async getItemsById(id){
        return await this.model.getItemsById(id)
    }
}