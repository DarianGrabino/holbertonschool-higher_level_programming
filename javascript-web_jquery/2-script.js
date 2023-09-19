// updates the text color of the <header> element to red when the user clicks
$(document).ready(function()
{
    $('#red_header').click(function()
    {
        var header = $('header');
        header.css('color', '#FF0000');
    });
});
