#!/usr/bin/node

const farg = process.argv[2];
if (farg === undefined) {
  console.log('Missing number of occurences');
} else {
  let i;
  for (i = 0; i < parseInt(farg); i++) {
    console.log('C is fun');
  }
}
