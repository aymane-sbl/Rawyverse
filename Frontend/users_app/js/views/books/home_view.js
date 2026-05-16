

export class HomeView{
    constructor(controller){
        this.controller = controller
    }
    init(){
        this.getItems()
    }
    // get all items
    async getItems(){
        let btnMenu = document.querySelector("#menu");
        let isClicked = false;
        
        btnMenu.addEventListener("click",()=>{
            isClicked = !isClicked;
            if(isClicked){
                document.querySelector(".container header .logo").style.display = "block";
                document.querySelector(".container header .profile-search").style.display = "block";
            }else{
                document.querySelector(".container header .logo").style.display = "none";
                document.querySelector(".container header .profile-search").style.display = "none";
            }
        });

        let main = document.querySelector("#home");
        let footer = document.querySelector("footer");
        

        
        
        try {
            let response = await this.controller.getItems();
            let data = response["data"];
            data.forEach((e) => {
                let section = document.createElement("section");
                let img = document.createElement("img");
                let h2 = document.createElement("h2");

                img.src = e["image_url"];
                h2.textContent = e["title"];
                section.classList.add("card");
                section.append(img);
                section.append(h2);
                
               
                main.append(section);

                 section.addEventListener("click",()=>{
                        window.location.href = `/users_app/pages/books/details.html?id=${e["id"]}`;
                            })
               

                // footer
                footer.innerHTML =" "
                for (let i = 1; i <= response["pagination"]["total_pages"]; i++) {
                    let button = document.createElement("button");
                    button.textContent = i;
                    footer.append(button)
                }
                
                });
             

           
            
        }catch (e){
            console.log(e)
        }
    }

}