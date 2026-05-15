import { validator } from "./utils/validator.js";
import { passwordVisiibility } from "./utils/password_visibility.js";

export class LoginView{
    constructor(controller){
        this.controller = controller
    }
    init(){
        this.login()
    }
    login(){
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
            try {
                let response = await this.controller.login(email.value,password.value);
                window.location.replace("/users_app/pages/books/home.html");
                
                
                
            } catch (error) {
                console.log(error.message);
            }
        })
        
    }
}
