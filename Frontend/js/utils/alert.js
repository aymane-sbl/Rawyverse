import Swal from "https://cdn.jsdelivr.net/npm/sweetalert2@11/+esm";
export function showAlert(title,message,icon){
     Swal.fire({
                            title: title,
                            text: message,
                            icon: icon
                        });
}