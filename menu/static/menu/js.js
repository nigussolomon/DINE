var update = document.getElementById("registerForm");
var updateBtn = document.getElementById("updateBtn");
var addBtn = document.getElementById("addrestaurant");
var restaurant = document.getElementById("restaurant");
var up = document.getElementById("up");

updateBtn.onclick = () => {
    update.style.transitionDelay = ".2s";
    update.style.transitionDuration = ".3s";
    update.style.top = "9%";
    restaurant.style.top = "-100%";
}

addBtn.onclick = () => {
    restaurant.style.transitionDelay = ".2s";
    restaurant.style.transitionDuration = ".3s";
    restaurant.style.top = "9%";
    update.style.top = "-100%";

}

up.onclick = () =>{
    restaurant.style.top = "9%"
    document.location.hash = 'form';
}

window.onload = () =>{
    restaurant.style.top = "9%"
}



