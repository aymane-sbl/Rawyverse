export function passwordVisiibility(passwordInput,passwordIcon){
    let isPassword=true;
    passwordIcon.addEventListener("click",(e)=>{
        isPassword =!isPassword
            if (isPassword){
            password.setAttribute("type","text");
            passwordIcon.textContent = 'visibility';
        }else{
            password.setAttribute("type","password");
            passwordIcon.textContent = 'visibility_off';
        }
        });
}