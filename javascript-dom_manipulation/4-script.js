// adds a li element to a list when the user clicks on the element with id add_item
var addbutton = document.getElementById("add_item");
var mylist = document.querySelector(".my_list");
addbutton.addEventListener("click", function()
{
    var createlist = document.createElement("li");
    createlist.textContent = "Item";
    mylist.appendChild(createlist);
})
