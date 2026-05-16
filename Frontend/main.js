
let rootes = {
    register :async ()=>{
        try {
            const {RegisterModels} = await import("./users_app/js/api/auth/register.js");
            const {RegisterControllers} = await import("./users_app/js/controllers/auth/register_controoler.js");
            const {RegisterView} = await import ("./users_app/js/views/auth/register_view.js");

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
            const {LoginModels} = await import("./users_app/js/api/auth/login_models.js");
            const {LoginController} = await import("./users_app/js/controllers/auth/login_controller.js");
            const {LoginView} = await import ("./users_app/js/views/auth/login_views.js");

            const loginModel = new LoginModels();
            const loginController = new LoginController(loginModel);
            const loginView =  new LoginView(loginController);
            loginView.init();

            }catch(error){
                console.log(error)
            }
        },
    home : async()=>{
        try {
            const {HomeModels} = await import("./users_app/js/api/books/home_models.js");
            const {HomeControllers}= await import("./users_app/js/controllers/books/home_Controllers.js");
            const {HomeView} =  await import("./users_app/js/views/books/home_view.js");

            const homeModels = new HomeModels();
            const homeControllers = new HomeControllers(homeModels);
            const homeView =  new HomeView(homeControllers);
            homeView.init()



        } catch (error) {
            console.log(error)
        }
    },
    details : async()=>{
        try {
            const {DetailsModels} = await import("./users_app/js/api/books/details_models.js");
            const {DetailsControllers}= await import("./users_app/js/controllers/books/details_controllers.js");
            const {DetailsView} =  await import("./users_app/js/views/books/details_view.js");

            const detailsModels = new DetailsModels();
            const detailsControllers = new DetailsControllers(detailsModels);
            const detailseView =  new DetailsView(detailsControllers);
            
            const urlParams = new URLSearchParams(window.location.search);
            let bookId = urlParams.get("id");
            
            detailseView.getItemsById(bookId);




        } catch (error) {
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

