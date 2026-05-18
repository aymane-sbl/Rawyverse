export class SearchController{
    constructor(models){
        this.models = models;
    }
    async search(title){
        return await this.models.search(title)
    }
}