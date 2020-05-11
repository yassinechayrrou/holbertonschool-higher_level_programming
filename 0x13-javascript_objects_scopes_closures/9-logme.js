#!/usr/bin/node

let counter = 0;
exports.logMe = function (item) {
  if (item) {
    console.log('%s: %s', counter, item);
    counter++;
  }
};
