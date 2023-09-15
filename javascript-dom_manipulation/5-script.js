// updates the text of the header element to New Header!!! when the user clicks
var updateheader = document.getElementById("update_header");
var header = document.querySelector("header");
updateheader.addEventListener("click", function()
{
    header.textContent = "New Header!!!";
});
