#!/usr/bin/node

const outer = require('./100-data.js');

const inner = outer.list.map(x => outer.list.indexOf(x) * x);

console.log(outer.list);
console.log(inner);
