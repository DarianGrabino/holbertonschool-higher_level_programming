// fetches the character name from a URL
$(document).ready(function()
{
    var characterURL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    $.ajax({
        url: characterURL,
        type: 'GET',
        dataType: 'json',
        success: function(data)
        {
            var characterName = data.name;
            $('#character').text(characterName)
        },
        error: function(error)
        {
            console.error('Error character data', error);
        }
    });
});
