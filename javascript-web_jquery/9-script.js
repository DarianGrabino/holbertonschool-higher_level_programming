// say hello
$(document).ready(function() {
    var url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    $.get(url, function(data) {
        $('#hello').text(data.hello);
    });
});
