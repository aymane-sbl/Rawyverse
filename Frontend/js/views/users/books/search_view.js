export class SearchView{
    constructor(controller){
        this.controller = controller;
    }
    async search(){
        
        let query = new URLSearchParams(window.location.search);
        let title = query.get("title");

        try {
            let main = document.querySelector("main");
            let response = await this.controller.search(title);
            let data = response["data"];
            data.forEach((e) => {
                let section = document.createElement("section");
                section.classList.add("card");
                let img = document.createElement("img");
                let h2 = document.createElement("h2");

                img.src=e["image_url"];
                img.alt = e["title"];
                h2.textContent = e["title"];

                section.append(img);
                section.append(h2);

                main.append(section);
                section.addEventListener("click",()=>{
                    window.location.href = `/pages/users/books/details.html?id=${e["id"]}`;
                })
            });
        } catch (error) {
            console.error(error)
        }
    }
}

