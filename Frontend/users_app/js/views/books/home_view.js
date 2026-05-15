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

