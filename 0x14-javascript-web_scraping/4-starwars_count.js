#!/usr/bin/node

const request = require('request');

function getTitle (url) {
  let count = 0;

  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else if (response.statusCode === 200) {
      const pageResults = JSON.parse(body);

      for (let i = 0; i < pageResults.count; i++) {
	      const myResults = pageResults.results[i];

	      const myChars = myResults.characters;
	      const countValue = myChars.includes(
		      'https://swapi-api.alx-tools.com/api/people/18/'
	      );

	      if (countValue) { count++; }
      }
      console.log(count);
    } else {
      console.error(`Error: Unexpected status code ${response.statuscode}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <url>');
  process.exit(1);
}

const url = process.argv[2];
getTitle(url);
