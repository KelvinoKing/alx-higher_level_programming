#!/usr/bin/node
const args = process.argv.slice(2);
const myInt = parseInt(args[0]);

if (!myInt) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myInt; i++) {
    console.log('C is fun');
  }
}
