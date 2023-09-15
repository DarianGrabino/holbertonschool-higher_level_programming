// updates the text color of the header to red when the user clicks on the tag
var redheader = document.getElementById("red_header");
redheader.addEventListener("click", function()
{
    var header = document. querySelector("header");
    header.style.color = "#FF0000";
});
