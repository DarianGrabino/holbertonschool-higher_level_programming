// updates the text of the <header> when the user clicks on DIV#update_header
$(document).ready(function()
{
    $('#update_header').click(function()
    {
        var header = $('header');
        header.text('New Header!!!');
    });
});
