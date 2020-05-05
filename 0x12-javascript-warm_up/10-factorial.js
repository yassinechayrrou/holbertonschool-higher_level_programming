#!/usr/bin/node

const farg = parseInt(process.argv[2]);
if (farg === undefined || isNaN(farg)) {
  console.log('1');
} else {
  let factorial = 1;
  let i;
  for (i = farg; i > 1; i--) {
    factorial = factorial * i;
  }
  console.log(factorial);
}
