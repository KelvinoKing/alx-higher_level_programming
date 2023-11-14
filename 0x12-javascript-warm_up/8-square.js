#!/usr/bin/node
const args = process.argv.slice(2);
const myInt = parseInt(args[0]);

if (!myInt) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myInt; i++) {
    let s = '';

    for (let j = 0; j < myInt; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
