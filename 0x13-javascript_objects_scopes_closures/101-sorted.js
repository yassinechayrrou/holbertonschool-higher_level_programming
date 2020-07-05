#!/usr/bin/node

const library = require('./101-data.js');

const vals = Object.values(library.dict);
let unique = [...new Set(vals)];
console.log(unique);
let larousse = {};

for (let i = 0; i < unique.length; i++) {
  let keys = Object.keys(library.dict).filter(function(key) {
    return library.dict[key] === unique[i]
  });
  larousse[unique[i]] = keys;
}
console.log(larousse);
