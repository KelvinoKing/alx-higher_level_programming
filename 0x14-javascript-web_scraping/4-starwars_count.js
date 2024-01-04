#!/usr/bin/node

const request = require('request');

function countMoviesWithCharacter (apiUrl, characterId) {
  let count = 0;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else if (response.statusCode === 200) {
      const films = JSON.parse(body).results;

      films.forEach(film => {
        const characters = film.characters.find(character => character.endsWith('/18/'));
        if (characters) {
          count++;
        }
      });

      console.log(count);
    } else {
      console.error(`Error: Unexpected status code ${response.statusCode}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node 4-starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18;

countMoviesWithCharacter(apiUrl, characterId);
