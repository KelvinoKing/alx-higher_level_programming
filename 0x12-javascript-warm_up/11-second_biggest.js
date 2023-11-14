#!/usr/bin/node
const args = process.argv.slice(2);
const lenArgs = args.length;

function largest (n) {
  let temp = n[0];
  let secLargest = -Infinity;

  for (let i = 0; i < n.length; i++) {
    if (n[i] > temp) {
      secLargest = temp;
      temp = n[i];
    } else if (n[i] > secLargest && n[i] !== temp) {
      secLargest = n[i];
    }
  }
  return secLargest;
}

if (lenArgs === 0 || lenArgs === 1) {
  console.log(0);
} else {
  const newArray = [];

  for (let i = 0; i < lenArgs; i++) {
    newArray.push(parseInt(args[i]));
  }
  console.log(largest(newArray));
}
