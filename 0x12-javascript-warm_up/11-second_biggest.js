#!/usr/bin/node
const arg = process.argv;
const argc = process.argv.length;
if (argc < 4) {
  console.log(0);
} else {
  let i;
  let arr = [];
  for (i = 0; i < argc; i++) {
    const elem = parseInt(arg[i]);
    if (!isNaN(elem)) {
      arr = arr.concat(elem);
    }
    arr = arr.sort();
  }
  console.log(arr[arr.length - 2]);
}
