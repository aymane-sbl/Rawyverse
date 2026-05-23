export class ProfileControllers{
    constructor(models){
        this.models = models
    }

    async getCurrentUser(){
        return await this.models.getCurrentUser();
    }
}