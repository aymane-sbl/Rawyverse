import {showAlert} from "../../../utils/alert.js"
import Swal from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";
export class LogoutViews{
    constructor(controller){
        this.controller = controller;
    }
    async logout(){
        let btnLogout = document.getElementById("logout");
        btnLogout.addEventListener("click",async (e)=>{
            e.preventDefault();
            try {
                Swal.fire({
                        allowOutsideClick : false,
                        didOpen(){
                            Swal.showLoading();
                        }
                    });

                let response = await this.controller.logout();
                window.location.replace("/pages/auth/login.html");
            }catch(error){
                showAlert("error",error.message,"error");

            }

        })

    }
}