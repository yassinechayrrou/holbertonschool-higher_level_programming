#!/usr/bin/node
const ac = process.argv.length;
if (ac === 3) {
  console.log('Arguement found');
} else if (ac < 3) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
