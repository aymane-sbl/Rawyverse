
import Swal  from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";
import {showAlert,showAlertLoading} from "../../utils/alert.js"

export class CategorieViews{
    constructor (controller){
        this.controller = controller
    }
    async init(){
        await this.addCategories()
        await this.deleteCategories()
    }
    async addCategories(){
        let nameInput = document.getElementById("title-add");
        let form = document.getElementById("form-add-categories");
        form.addEventListener("submit",async (e)=>{
            e.preventDefault();
            showAlertLoading();
            try{
                let response = await this.controller.addCategories(nameInput.value);
                Swal.fire({
                    title : "Success",
                    text:response["msg"],
                    icon : "success"
                })
            }catch(error){
                 showAlert("error",error.message,"error");
            }
        })
    }
    // delete  caetgories
    async deleteCategories(){
        let nameInput = document.getElementById("title-delete");
        let form = document.getElementById("form-delete-categories");
        form.addEventListener("submit",async (e)=>{
            e.preventDefault();
            showAlertLoading()
            try{
                let response = await this.controller.deleteCategories(nameInput.value);
                Swal.fire({
                    title : "Success",
                    text:response["msg"],
                    icon : "success"
                })
            }catch(error){
                showAlert("error",error.message,"error");
            }
        })
    }
}