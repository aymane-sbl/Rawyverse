import Swal  from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";
export class ItemsViews{
    constructor(controller){
        this.controller = controller
    }
    async init(){
        await this.addItems()
        await this.deleteItems()
    }
    async addItems(){
         let form = document.getElementById("form-add-item");
        form.addEventListener("submit",async (e)=>{
            e.preventDefault();
            try {
               
                let formData = new FormData(form);
                
                let response = await this.controller.addItems(formData);
                Swal.fire({
                    "title" : "Success",
                    "text" : response["msg"],
                    icon : "success"
                    });
            }catch(error){
                console.log(error)
            }
        })
        
    }
    async deleteItems(){
        let form = document.getElementById("form-delete-item");
        form.addEventListener("submit",async(e)=>{
            e.preventDefault()
            try{
                let titleInput = document.getElementById("title-delete");
                let response = await this.controller.deleteItems(titleInput.value);
                Swal.fire({
                    "title" : "Success",
                    "text" : response["msg"],
                    icon : "success"
                    });
            }catch(error){
                console.log(error)
            }
            
        })
    }
}