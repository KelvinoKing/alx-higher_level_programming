#!/usr/bin/node
const args = process.argv.slice(2);
const lenArgs = args.length;

if (lenArgs === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
