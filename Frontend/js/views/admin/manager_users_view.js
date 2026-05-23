import Swal from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";
import {showAlert} from "../../utils/alert.js"
export class ManagerUsersView{
    constructor(controller){
        this.controller = controller;
    }
    async init(){
        await this.deleteUsers()
    } 
    async deleteUsers(){
        let emailInput = document.getElementById("email");
        let form = document.getElementById("form-delete-users");
        form.addEventListener("submit",async (e) => {
            e.preventDefault()
            try{
                let response = await this.controller.deleteUsers(emailInput.value);
                Swal.fire({
                    title : "success",
                    text : response["msg"],
                    icon : "success"
                })

            }catch(error){
                showAlert("error",error.message,"error");

            }
        })
    }
}