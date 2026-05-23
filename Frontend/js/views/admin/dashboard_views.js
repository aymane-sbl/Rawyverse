import {showAlert} from "../../utils/alert.js"
export class DashbordsViews{
    constructor(itemsControllers,usersControllers){
        this.itemsControllers = itemsControllers;
        this.usersControllers = usersControllers;
    }
    __createCards(main,title,response){
            let section = document.createElement("section");
            section.classList.add("card")
            let h2 = document.createElement("h2");;
            let h3 = document.createElement("h3");
            h2.textContent = title;
            h3.textContent = response["length"];

            section.append(h2);
            section.append(h3);
            main.append(section);
    }
    async Dashbord(){
        const main  = document.querySelector("main");
        
        try {
            let userResponse = await this.usersControllers.getLengthUsers();
            let itemsResponse = this.itemsControllers
            this.__createCards(main,"عدد المستخدمين",userResponse);
            this.__createCards(main,"مجموع الكتب والروايات",await itemsResponse.totalItems());
            this.__createCards(main,"مجموع الكتب",await itemsResponse.totalBooks());
            this.__createCards(main,"مجموع الروايات",await itemsResponse.totalNovels());
        } catch (error) {
            howAlert("error",error.message,"error");

        }
    }
}