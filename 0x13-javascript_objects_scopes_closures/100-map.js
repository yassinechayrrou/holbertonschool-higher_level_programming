#!/usr/bin/node

const outer = require('./100-data.js');

const inner = outer.list.map((x, index) => {
  return x * index;
});

console.log(outer.list);
console.log(inner);
