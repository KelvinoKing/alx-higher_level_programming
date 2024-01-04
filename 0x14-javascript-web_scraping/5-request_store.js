#!/usr/bin/node

const request = require('request');
const fs = require('fs');

function writeBody (url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else if (response.statusCode === 200) {
      const data = body;
      fs.writeFile(filePath, data,
        {
          encoding: 'utf8',
          flag: 'w'
        },
        (err) => {
          if (err) { console.log(err); }
        });
    } else {
      console.error('Error: Unexpected status code');
    }
  });
}

if (process.argv.length < 4) {
  console.error('Usage: node 1-writeme.js <filepath> <data>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

writeBody(url, filePath);
