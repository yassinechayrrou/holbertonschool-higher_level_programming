#!/usr/bin/node
const ac = process.argv.length;
if (ac === 2) {
  console.log('No arguement');
} else if (ac === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
