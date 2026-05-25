
export class LogoutController{
    constructor(models){
        this.models = models;
    }
    async logout(){
        return await this.models.logout();

    }
}