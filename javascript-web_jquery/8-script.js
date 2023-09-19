//  fetches and lists the title for all movies by using a URL
$(document).ready(function()
{
    var moviesURL = 'https://swapi-api.hbtn.io/api/films/?format=json';
    $.ajax({
        url: moviesURL,
        type: 'GET',
        dataType: 'json',
        success: function(data)
        {
            var movies = data.results;
            var listmovie = $('#list_movies');
            movies.forEach(function(movies)
            {
                var title = movie.title;
                var list = $('<li>').text(title);
                listmovie.append(list);
            });
        },
        error: function(error)
        {
            console.error('Error movie data', error);
        }

    });
});
