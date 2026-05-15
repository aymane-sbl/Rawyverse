
let rootes = {
    register :async ()=>{
        try {
            const {RegisterModels} = await import("./js/api/auth/register.js");
            const {RegisterControllers} = await import("./js/controllers/auth/register_controoler.js");
            const {RegisterView} = await import ("./js/views/auth/register_view.js");

            const registerModel = new RegisterModels()
            const registerController = new RegisterControllers(registerModel)
            const registerView = new RegisterView(registerController)

            registerView.init()

        }catch(error){
            console.log(error)
        }
    },
    login : async ()=>{
            try {
            const {LoginModels} = await import("./js/api/auth/login_models.js");
            const {LoginController} = await import("./js/controllers/auth/login_controller.js");
            const {LoginView} = await import ("./js/views/auth/login_views.js");

            const loginModel = new LoginModels();
            const loginController = new LoginController(loginModel);
            const loginView =  new LoginView(loginController);
            loginView.init();

            }catch(error){
                console.log(error)
            }
        }
}

let currentPath = window.location.pathname.toLowerCase();
let pageFound = false;

for (let route in rootes){
    if (currentPath.includes(route)){
        rootes[route]();
        pageFound = true;
        break;

    }

}

if (!pageFound){
    console.log("page not found");
}

