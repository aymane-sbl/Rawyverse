export class DetailsView{   
    constructor(controller){
        this.controller = controller
    }   // get items by id
    async getItemsById(id){
        let main = document.querySelector("main");
        // section
        let section = document.createElement("section");
        section.classList.add("details");
        // image
        let imageDiv = document.createElement("div");
        let img= document.createElement("img");
        imageDiv.classList.add("image");
        // info
        let infoDiv= document.createElement("div");
        infoDiv.classList.add("info");
        // btns
        let btnDiv = document.createElement("div");
        let button = document.createElement("button");
        let a = document.createElement("a");
        btnDiv.classList.add("btns");
        button.append(a);
        // synopsis
        let synopsis = document.createElement("article");
        synopsis.classList.add("synopsis")
        try {
            let response = await this.controller.getItemsById(id);
            let data = response["data"];

            img.src = data["image_url"];
            imageDiv.append(img);
            let content = [
              `العنوان : ${data["title"]}`  ,
              `المؤلف : ${data["author"]}`  ,
              `اللغة : ${data["language"]}`  ,
              `سنة النشر : ${data["year"]}`  ,
              `عدد الصفحات : ${data["pages"]}`  ,
              
            ]
            content.forEach((e)=>{
                const p = document.createElement("p");
                p.textContent = e;
                infoDiv.append(p);
            })
            
            let genres = JSON.parse(data["genres"]);
            const p = document.createElement("p");
                p.textContent = ` التصنيفات الفنية :${ genres.join(" , ")}`;
                infoDiv.append(p);

            section.append(imageDiv);
            section.append(infoDiv);

            // links
            a.href = data["file_url"];
            a.textContent ="ابدأ القراءة";
            button.append(a);
            btnDiv.append(button);
            // synopsi
            let synpsisText = data["synopsis"];
            synopsis.append(synpsisText);

        
            

            main.append(section);
            main.append(btnDiv);
            main.append(synopsis)
        }catch (e){
            console.log(e)
        }



    }

}