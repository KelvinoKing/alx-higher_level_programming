#!/usr/bin/node

const request = require('request');

function getTitle (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else if (response.statusCode === 200) {
      const title = JSON.parse(body);
      console.log(title.title);
    } else {
      console.error(`Error: Unexpected status code ${response.statuscode}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <url>');
  process.exit(1);
}

const nameId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${nameId}`;
getTitle(url);
