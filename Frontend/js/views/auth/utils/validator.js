export function validator(input,id,regex_pattern) {
    if(input === "" || regex_pattern.test(input) === false){
            document.querySelector(id).style.display = "block";
        }else{
            document.querySelector(id).style.display = "none";
        }
}