export class BooksController{
    constructor (models){
        this.models = models;
    }
    async getBooks(){
        return this.models.getBooks()
    }
}