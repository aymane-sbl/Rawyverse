import { get_specific_items_category_views } from "../../../shared/view/get_specific_items_category_views.js";
export class NovelsView{
    constructor (controller){
        this.controller = controller;
    }
    async getNovels(){
        let controller = await this.controller.getNovels()
        get_specific_items_category_views(controller)
    }
}

// try {
//             let main = document.querySelector("main")
//             let response = await this.controller.getNovels();
//             let data = response["data"];
//             data.forEach((e) => {
//                 const section = document.createElement("section");
//                 section.classList.add("card");
//                 let img = document.createElement("img");
//                 let h2 = document.createElement("h2");
                
//                 img.src = e["image_url"];
//                 img.alt = e["title"];
//                 h2.textContent = e["title"];

//                 section.append(img);
//                 section.append(h2);
//                 main.append(section);

//             });
//         } catch (error) {
//             console.log(error)
//         }