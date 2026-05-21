export class ItemsController{
    constructor(models){
        this.models = models
    }
    async addItems(form){
        return await this.models.addItems(form)
    }
    async deleteItems(title){
        return await this.models.deleteItems(title)
    }
}