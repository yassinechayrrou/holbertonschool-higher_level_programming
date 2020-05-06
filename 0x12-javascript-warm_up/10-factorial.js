#!/usr/bin/node

const farg = parseInt(process.argv[2]);
function factorial (n) {
  if (n === undefined || isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(farg));
