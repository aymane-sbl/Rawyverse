import { validator } from "./utils/validator.js";
import {passwordVisiibility} from "./utils/password_visibility.js";
import { showAlert } from "../../utils/alert.js";
import Swal from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";



export class RegisterView{
    constructor(controllers){
        this.controllers = controllers;
    }
    init(){
        this.register();
    }
    register(){
        let userName=document.querySelector("#username");
        let email = document.querySelector("#email");
        let password= document.querySelector("#password");
        let passwordIcon = document.querySelector("#password-icon");
        let submitBtn = document.querySelector("input[type='submit']");
        let form = document.querySelector("form");

        // password visibility
        passwordVisiibility(password,passwordIcon);

        // check input validation
        userName.addEventListener("blur",()=>{
            validator(userName.value,"#username-error",/^[a-zA-Z][a-zA-Z0-9_]{2,}$/);
        })
        email.addEventListener("blur",()=>{
            validator(email.value,"#email-error",/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/);
        })

        password.addEventListener("blur",()=>{
            validator(password.value,"#password-error",/^.{8,}$/);
        })

        // submit
        form.addEventListener("submit",async (e)=>{
            e.preventDefault();
            Swal.fire({
                            allowOutsideClick : false,
                            didOpen(){
                                Swal.showLoading();
                            }
                        });
            try {
            validator(userName.value,"#username-error",/^[a-zA-Z][a-zA-Z0-9_]{2,}$/);
            validator(email.value,"#email-error",/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/);
            validator(password.value,"#password-error",/^.{8,}$/);
            let response = await this.controllers.register(userName.value,email.value,password.value);
                 showAlert("Success",response["message"],"success");
            } catch (error) {
               showAlert("Error",error.message,"error");
            }
        })
        
    }


}
