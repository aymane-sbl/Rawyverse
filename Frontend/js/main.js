
let rootes = {
    register :async ()=>{
        try {
            const {RegisterModels} = await import("./api/auth/register.js");
            const {RegisterControllers} = await import("./controllers/auth/register_controoler.js");
            const {RegisterView} = await import ("./views/auth/register_view.js");

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
            const {LoginModels} = await import("./api/auth/login_models.js");
            const {LoginController} = await import("./controllers/auth/login_controller.js");
            const {LoginView} = await import ("./views/auth/login_views.js");

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
            const {HomeModels} = await import("./api/users/home_models.js");
            const {HomeControllers}= await import("./controllers/users/home_Controllers.js");
            const {HomeView} =  await import("./views/users/home_view.js");

            const homeModels = new HomeModels();
            const homeControllers = new HomeControllers(homeModels);
            const homeView =  new HomeView(homeControllers);
            
            await homeView.init()



        } catch (error) {
            console.log(error)
        }
    },
    details : async()=>{
        try {
            const {DetailsModels} = await import("./api/users/books/details_models.js");
            const {DetailsControllers}= await import("./controllers/users/books/details_controllers.js");
            const {DetailsView} =  await import("./views/users/books/details_view.js");

            const detailsModels = new DetailsModels();
            const detailsControllers = new DetailsControllers(detailsModels);
            const detailseView =  new DetailsView(detailsControllers);
            
            const urlParams = new URLSearchParams(window.location.search);
            let bookId = urlParams.get("id");
            
            detailseView.getItemsById(bookId);




        } catch (error) {
            console.log(error)
        }
    },
    search : async ()=>{
            try {
                const {SearchModels} = await import("./api/users/books/search_models.js");
            const {SearchController}= await import("./controllers/users/books/search_controllers.js");
            const {SearchView} =  await import("./views/users/books/search_view.js");

            const searchModels = new SearchModels();
            const searchControllers = new SearchController(searchModels);
            const searchView =  new SearchView(searchControllers);

            await searchView.search()
            } catch (error) {
                 console.log(error)
            }
    },
    novels : async ()=>{
         try {
            const {NovelsModels} = await import("./api/users/books/novels_models.js");
            const {NovelsController}= await import("./controllers/users/books/novels_controller.js");
            const {NovelsView} =  await import("./views/users/books/novels_view.js");

            const novelsModels = new NovelsModels();
            const novelsControllers = new NovelsController(novelsModels);
            const novelsView =  new NovelsView(novelsControllers);

            await novelsView.getNovels()
            } catch (error) {
                 console.log(error)
            }
    },
    books : async ()=>{
         try {
            const {BooksModels} = await import("./api/users/books/books_models.js");
            const {BooksController}= await import("./controllers/users/books/books_controller.js");
            const {BooksView} =  await import("./views/users/books/books_view.js");

            const booksModels = new BooksModels();
            const booksControllers = new BooksController(booksModels);
            const booksView =  new BooksView(booksControllers);

            await booksView.getBooks()
            } catch (error) {
                 console.log(error)
            }
    },
    items : async()=>{
            const {ItemsModels} = await import("./shared/models/admin/items_models.js");
            const {ItemsController}= await import("./shared/controller/admin/items_controllers.js");
            const {ItemsViews} =  await import("./views/admin/items_view.js");

            const itemsModels = new ItemsModels();
            const itemssControllers = new ItemsController(itemsModels);
            const itemsView =  new ItemsViews(itemssControllers);
            itemsView.init()
            

    },
    users : async()=>{
            const {ManagerUsersModels} = await import("./shared/models/admin/manager_users_models.js");
            const {ManagerUsersController}= await import("./shared/controller/admin/manager_users_controller.js");
            const {ManagerUsersView} =  await import("./views/admin/manager_users_view.js");

            const models = new ManagerUsersModels();
            const controller = new ManagerUsersController(models);
            const view =  new ManagerUsersView(controller);
            view.init()
            

    },
    category : async ()=>{
            const {CategorieModels} = await import("./shared/models/admin/categories_models.js");
            const {CategorieController}= await import("./shared/controller/admin/categories_controller.js");
            const {CategorieViews} =  await import("./views/admin/categories_views.js");

            const models = new CategorieModels();
            const controller = new CategorieController(models);
            const view =  new CategorieViews(controller);
            view.init()
    },
    dashbord : async ()=>{
        // users
            const {ManagerUsersModels} = await import("./shared/models/admin/manager_users_models.js");
            const {ManagerUsersController}= await import("./shared/controller/admin/manager_users_controller.js");
            const uModels = new ManagerUsersModels();
            const uController = new ManagerUsersController(uModels);
        // items
            const {ItemsModels} = await import("./shared/models/admin/items_models.js");
            const {ItemsController}= await import("./shared/controller/admin/items_controllers.js");
            const itemsModels = new ItemsModels();
            const itemsControllers = new ItemsController(itemsModels);
        // dashborad
        let {DashbordsViews} = await import("./views/admin/dashboard_views.js");
        let dashboardViews =new DashbordsViews(itemsControllers,uController);
        await dashboardViews.Dashbord()
    },
    profile : async ()=>{
            const {ProfileModels} = await import("./api/users/profile/profile_models.js");
            const {ProfileControllers}= await import("./controllers/users/profile/profile_controller.js");
            const {ProfileViews} =  await import("./views/users/profile/profile_views.js");

            const models = new ProfileModels();
            const controller = new ProfileControllers(models);
            const view =  new ProfileViews(controller);
            await view.init()
    }

}


let currentPath = window.location.pathname.toLowerCase();
let pageName = currentPath.split("/").pop().replace(".html","");
if (pageName === "" || pageName == "index"){
    pageName = "home";
}
if (rootes[pageName]){
    rootes[pageName]();
}else {
    window.location.replace("/pages/not_found.html")
}

