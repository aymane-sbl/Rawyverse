import { validator } from "./utils/validator.js";
import { passwordVisiibility } from "./utils/password_visibility.js";
import { showAlert } from "../../utils/alert.js";
import Swal from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";

export class LoginView{
    constructor(controller){
        this.controller = controller
    }
    async init(){
        await this.login()
        await this.loginWithGoogle()
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
    // loginWithGoogle
    async loginWithGoogle(){
        const firebaseConfig = {
                apiKey: "AIzaSyBVi3ku7_uGQ02p9E9wEvp20DQQOZZrxF0",
                authDomain: "rawyverse.firebaseapp.com",
                projectId: "rawyverse",
                storageBucket: "rawyverse.firebasestorage.app",
                messagingSenderId: "721229655572",
                appId: "1:721229655572:web:0ecf1b6e98189b84984101"
                };
        const app = initializeApp(firebaseConfig);
        const auth = getAuth(app);
        const provider = new GoogleAuthProvider();

        let btn = document.getElementById("google-btn");
        btn.addEventListener("click",async (e)=>{
            e.preventDefault()
                let result = await signInWithPopup(auth,provider);
                let token = await result.user.getIdToken();
                try {
                    let response = await this.controller.loginWithGoogle(token);
                    if (response["role"] === "admin"){
                        window.location.replace("/pages/admin/dashbord.html");
                        console.log(result)
                    }else{
                            window.location.replace("/pages/users/home.html");
                        console.log(result)

                        }
                        

                } catch (error) {
                    showAlert("Error",error.message,"error");
                }
        })
    }
}
