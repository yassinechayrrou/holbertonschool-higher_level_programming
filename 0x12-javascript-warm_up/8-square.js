#!/usr/bin/node

const farg = parseInt(process.argv[2]);
if (farg === undefined) {
  console.log('Missing size');
} else if (isNaN(farg)) {
  console.log('Missing size');
} else {
  let i;
  const square = 'X';
  for (i = 0; i < farg; i++) {
    console.log(square.repeat(farg));
  }
}
