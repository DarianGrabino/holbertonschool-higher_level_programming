// toggles the class of the header 
var header = document.querySelector("header");
var toggleheader = document.getElementById("toggle_header");
toggleheader.addEventListener("click", function()
{
    if (header.classList.contains("red"))
    {
        header.classList.remove("red");
        header.classList.add("green");
    }
    else
    {
        header.classList.remove("green");
        header.classList.add("red");
    }
});
