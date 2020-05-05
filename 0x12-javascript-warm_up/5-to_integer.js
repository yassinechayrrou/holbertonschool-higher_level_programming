#!/usr/bin/node

const farg = process.argv[2];
if (farg === undefined) {
  console.log('Not a number');
} else if (isNaN(farg) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + farg);
}
