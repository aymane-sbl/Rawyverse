import Swal from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";

export async function initApi(endpoints,options={methode : "GET"}) {
    const baseUrl = "http://127.0.0.1:8000";
    let response = await fetch(`${baseUrl}${endpoints}`,options);
    if (!response.ok){
        let errorMsg = await response.json();

        Swal.fire({
        title: "Error",
        text: errorMsg["detail"],
        icon: "error"
        });
        throw new Error(errorMsg["detail"]);
        
    }
    let data = await response.json();
    return data
}

