#!/usr/bin/node

const dict = require('./101-data.js').dict;

const larousse = {};

for (const key in dict) {
  if (larousse[dict[key]] === undefined) {
    larousse[dict[key]] = [];
  }
  larousse[dict[key]].push(key);
}
console.log(larousse);
