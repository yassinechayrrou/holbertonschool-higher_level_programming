#!/usr/bin/node

const argc = process.argv.length;
if (argc < 4) {
  console.log('NaN');
} else {
  const one = parseInt(process.argv[2]);
  const two = parseInt(process.argv[3]);
  console.log(String(one + two));
}
