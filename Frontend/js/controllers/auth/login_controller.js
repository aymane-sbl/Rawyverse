export class LoginController{
    constructor(model){
        this.model = model;
    }
    async login(email,password){
        return await this.model.login(email,password);
    }
}