#!/usr/bin/node

const farg = process.argv[2];
if (farg === undefined) {
  console.log('1');
} else {
  let factorial = 1;
  let i;
  for (i = parseInt(farg); i > 1; i--) {
    factorial = factorial * i;
  }
  console.log(factorial);
}
