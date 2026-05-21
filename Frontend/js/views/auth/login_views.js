import { validator } from "./utils/validator.js";
import { passwordVisiibility } from "./utils/password_visibility.js";
import { showAlert } from "../../utils/alert.js";
import Swal from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";

export class LoginView{
    constructor(controller){
        this.controller = controller
    }
    init(){
        this.login()
    }
    async login(){
        let email = document.querySelector("#email");
        let password= document.querySelector("#password");
        let passwordIcon = document.querySelector("#password-icon");
        let submitBtn = document.querySelector("input[type='submit']");

         // password visibility
        passwordVisiibility(password,passwordIcon)
         // check input validation
        email.addEventListener("blur",()=>{
                    validator(email.value,"#email-error",/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/);
                })
        
        password.addEventListener("blur",()=>{
                    validator(password.value,"#password-error",/^.{8,}$/);
                })

        // submit btn
        submitBtn.addEventListener("click" ,  async (e)=>{
            e.preventDefault();
            Swal.fire({
                allowOutsideClick : false,
                didOpen(){
                    Swal.showLoading();
                }
            });
            try {
                let response = await this.controller.login(email.value,password.value);
                if (response["role"] === "admin"){
                    window.location.replace("/pages/admin/dashbord.html");
                }else{
                    window.location.replace("/pages/users/home.html");
                }
                
                
                
            } catch (error) {
                showAlert("Error",error.message,"error");
                            
            }
        })
        
    }
}
