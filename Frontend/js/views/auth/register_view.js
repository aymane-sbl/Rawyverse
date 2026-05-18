import { validator } from "./utils/validator.js";
import {passwordVisiibility} from "./utils/password_visibility.js";
import Swal from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";


export class RegisterView{
    constructor(controllers){
        this.controllers = controllers
    }
    init(){
        this.register()
    }
    register(){
        let userName=document.querySelector("#username");
        let email = document.querySelector("#email");
        let password= document.querySelector("#password");
        let passwordIcon = document.querySelector("#password-icon");
        let submitBtn = document.querySelector("input[type='submit']");

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
        submitBtn.addEventListener("click",async (e)=>{
            e.preventDefault();
            try {
            validator(userName.value,"#username-error",/^[a-zA-Z][a-zA-Z0-9_]{2,}$/);
            validator(email.value,"#email-error",/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/);
            validator(password.value,"#password-error",/^.{8,}$/);
            let response = await this.controllers.register(userName.value,email.value,password.value)
            Swal.fire({
                    title: "Success",
                    text: response["message"],
                    icon: "success"
                    });
                console.log(response)
            } catch (error) {
                console.log(error.message)
            }
        })
        
    }


}
