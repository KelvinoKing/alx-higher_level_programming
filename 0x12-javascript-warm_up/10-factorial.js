#!/usr/bin/node
const args = process.argv.slice(2);
const myInt = parseInt(args[0]);

const factorial = (n) => {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
};

if (!myInt) {
  console.log(1);
} else {
  console.log(factorial(myInt));
}
