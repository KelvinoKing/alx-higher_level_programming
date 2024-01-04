#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Usage: node 1-writeme.js <filepath> <data>');
  process.exit(1);
}

const filePath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filePath, data,
  {
    encoding: 'utf8',
    flag: 'w'
  },
  (err) => {
    if (err) { console.log(err); }
  }
);
