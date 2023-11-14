#!/usr/bin/node
const args = process.argv.slice(2);
const lenArgs = args.length;

if (lenArgs === 0) {
  console.log('No argument');
} else if (lenArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
