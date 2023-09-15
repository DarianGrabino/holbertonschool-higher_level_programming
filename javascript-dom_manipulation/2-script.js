// class red to the header element when the user clicks
var redheader = document.getElementById("red_header");
redheader.addEventListener("click", function()
{
    var header = document.querySelector("header");
    header.classList.add("red");
});
