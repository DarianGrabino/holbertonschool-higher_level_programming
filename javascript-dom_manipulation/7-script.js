// get and list title of all movies using this url
var listMoviesElement = document.getElementById("list_movies");
var apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";

fetch(apiUrl)
  .then(function(response) {
    if (response.status === 200) {
      return response.json();
    } else {
      throw new Error("Failed to fetch movie data");
    }
  })
  .then(function(data) {
    data.results.forEach(function(movie) {
      var listItem = document.createElement("li");
      listItem.textContent = movie.title;
      listMoviesElement.appendChild(listItem);
    });
  })
  .catch(function(error) {
    console.error(error);
  });