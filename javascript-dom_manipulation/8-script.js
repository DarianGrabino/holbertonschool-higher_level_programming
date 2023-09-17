// get and display the value hello
document.addEventListener("DOMContentLoaded", function () {

    var helloElement = document.getElementById("hello");
  
    var apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  
    fetch(apiUrl)
      .then(function (response) {
        if (response.status === 200) {
          return response.json();
        } else {
          throw new Error("Failed to fetch translation data");
        }
      })
      .then(function (data) {
        helloElement.textContent = data.hello;
      })
      .catch(function (error) {
        console.error(error);
      });
  });
