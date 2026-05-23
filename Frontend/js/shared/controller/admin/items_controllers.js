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
    // total items
    async totalItems(){
        return await this.models.totalItems()
    }
     // total books
    async totalBooks(){
        return await this.models.totalBooks()
    }
    // total Noovels
    async totalNovels(){
        return await this.models.totalNovels()
    }
}