import { showAlert } from "../../../utils/alert.js";
export class ProfileViews{
    constructor(controller){
        this.controller = controller
    }
    async init(){
        await this.getCurrentUser()
    }
    async getCurrentUser(){
        let userNameInput = document.getElementById("username");
        let emailInput = document.getElementById("email");

        try {
            let response = await this.controller.getCurrentUser();
            userNameInput.value = response["user_name"];
            emailInput.value = response["email"];
        } catch (error) {
                let alert = await showAlert("error",error.message,"error");
                if(alert.isConfirmed){
                window.location.replace("/pages/auth/login.html");
                }
            }
        }
    
}