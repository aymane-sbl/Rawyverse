

export async function initApi(endpoints,options={method : "GET",credentials : "include",cache : "no-store"}) {
    const baseUrl ="https://api.rawyverse.xyz";
    let container =
document.querySelector(".container");
    GlobalLoader("block");
     container.innerHTML = "";
   try{
      let response = await fetch(`${baseUrl}${endpoints}`,options);
       if (!response.ok){
           let errorMsg = await response.json();
           
            throw new Error(errorMsg["detail"]);
           
       }
        
       let data = await response.json();
       return data
   }catch(error){
    throw error
   }finally{
    GlobalLoader("none");
   }
   }



function GlobalLoader(status) {
    let loader = document.getElementById("loader");
    if(loader){
        loader.style.display = status;
    }
}

