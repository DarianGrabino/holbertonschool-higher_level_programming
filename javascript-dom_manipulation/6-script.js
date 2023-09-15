// fetches the character name from a URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    var characterName = data.name;

    var characterElement = document.getElementById("character");

    characterElement.textContent = characterName;
  })
  .catch(error => console.error('Error:', error));
