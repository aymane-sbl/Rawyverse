export class ManagerUsersController{
    constructor (models){
        this.models = models
    }
    async deleteUsers(email){
        return await this.models.deleteUsers(email)
    }
    async getLengthUsers(){
        return await this.models.getLengthUsers()
    }
}