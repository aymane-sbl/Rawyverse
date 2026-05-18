export class NovelsController{
    constructor (models){
        this.models = models;
    }
    async getNovels(){
        return await this.models.getNovels()
    }
}