

export class HomeView{
    constructor(controller){
        this.controller = controller
    }
    init(){
        this.getItems()
        this.search()
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

        let main = document.querySelector("main");
        let footer = document.querySelector("footer");
        try {
            let quey = new URLSearchParams(window.location.search);
            let currentPage = quey.get("page") || 1
            let response = await this.controller.getItems(currentPage);
            let data = response["data"];
            data.forEach((e) => {
                let section = document.createElement("section");
                let img = document.createElement("img");
                let h2 = document.createElement("h2");

                img.src = e["image_url"];
                img.alt = e["title"]
                h2.textContent = e["title"];
                section.classList.add("card");
                section.append(img);
                section.append(h2);

                main.append(section);

                 section.addEventListener("click",()=>{

                        window.location.href = `/pages/users/books/details.html?id=${e["id"]}`;
                            })
                
                });
                 // footer
              
                for (let i = 1; i <= response["pagination"]["total_pages"]; i++) {
                    let button = document.createElement("button");
                    button.textContent = i;
                    footer.append(button)
                    if (i=== response["pagination"]["current_page"]){
                        button.style.borderColor = "red"
                    }
                    // click
                    button.addEventListener("click",()=>{
                        window.location.href = `?page=${i}`
                    })
                }
             

           
            
        }catch (e){
            console.log(e)
            
            }
        
    }
    search(){
        let searchBtn = document.querySelector("#search-icon");
        let form = document.querySelector("form");
        let searchInput = document.querySelector("#search-input");
        searchBtn.addEventListener("click",()=>{
            window.location.href = `/pages/users/books/search.html?title=${searchInput.value}`
        })

        form.addEventListener("submit",(e)=>{
                e.preventDefault();
             window.location.href = `/pages/users/books/search.html?title=${searchInput.value}`
        })
         
    }

}