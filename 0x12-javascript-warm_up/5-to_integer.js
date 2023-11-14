#!/usr/bin/node
const args = process.argv.slice(2);
const myInt = parseInt(args[0]);

if (!myInt) {
  console.log('Not a number');
} else {
  console.log('My number:', myInt);
}
