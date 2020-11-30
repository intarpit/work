
// Change of color for the selected (active) menu bar item.
let currentLocation = location.href;
currentLocation = currentLocation.split('?')[0]
let menuItem = document.querySelectorAll('li a');
let menuLength = menuItem.length;
for (let i = 0; i < menuLength; i++){
  if (menuItem[i].href === currentLocation){
    menuItem[i].className += " active" + " act";
    if (menuItem[i].parentElement.previousElementSibling.id == "navbarDropdown"){
      menuItem[i].parentElement.previousElementSibling.className += " active act";
    }; 
    // menuItem[i].parentElement.parentElement.className += " active act"; 
    // !This code also work but not perfect as it changes the ul class to active from non-dropdown menu items.
  };
}


// Menu bar on top while scrolling.
let height = $('header').height();
$(window).scroll(function (){
  if ($(this).scrollTop()> height){
    $('#nav').addClass('fixed-top');
  } else{
    $('#nav').removeClass('fixed-top');
  };
})


// Google map on contact us page.
"use strict";
function initMap() {
  let location = {lat: 24.578540, lng: 73.699360}
  let map = new google.maps.Map(document.getElementById("map"), {
    center: location,
    zoom: 15
  });
  let marker = new google.maps.Marker({
    position: location,
    map: map
  });
}
