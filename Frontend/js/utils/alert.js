import Swal from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";
export async function showAlert(title,message,icon){
    let result = Swal.fire({
                            title: title,
                            text: message,
                            icon: icon
                        });
    return result
}

export function showAlertLoading(){
     Swal.fire({
                allowOutsideClick : false,
                didOpen(){
                    Swal.showLoading();
                }
            });
}