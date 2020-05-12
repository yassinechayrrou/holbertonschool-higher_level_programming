#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const obj = JSON.parse(body);
  const dict = {};
  obj.forEach(function (objResults) {
    if (dict[objResults.userId] === undefined) {
      dict[objResults.userId] = 0;
    }
    if (objResults.completed === true) {
      dict[objResults.userId] += 1;
    }
  });
  console.log(dict);
});
