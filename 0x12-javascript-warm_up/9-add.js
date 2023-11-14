#!/usr/bin/node
const args = process.argv.slice(2);
const a = parseInt(args[0]);
const b = parseInt(args[1]);

if (!a || !b) {
  console.log('NaN');
} else {
  add(a, b);
}

function add (a, b) {
  console.log(a + b);
}
