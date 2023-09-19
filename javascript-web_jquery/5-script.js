// Create list of elements
$(document).ready(function()
{
    $('#add_item').click(function()
    {
        var createlist = $('<li>Item</li>');
        $('.my_list').append(createlist);
    });
});
