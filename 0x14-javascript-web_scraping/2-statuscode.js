#!/usr/bin/node

const request = require('request');

function getStatuscode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <url>');
  process.exit(1);
}

const url = process.argv[2];
getStatuscode(url);
