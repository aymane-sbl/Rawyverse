export class CategorieController{
    constructor(modules){
        this.module = modules;
    }
    async addCategories(name){
        return this.module.addCategories(name)
    }
    async deleteCategories(name){
        return this.module.deleteCategories(name)
    }
}