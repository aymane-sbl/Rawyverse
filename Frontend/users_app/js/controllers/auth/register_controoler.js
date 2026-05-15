export class RegisterControllers{
    constructor(models){
        this.models = models
    }
    async register(userName,email,password){
        return await this.models.register(userName,email,password)
    }
}