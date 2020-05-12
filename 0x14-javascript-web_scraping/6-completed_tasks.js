#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const obj = JSON.parse(body);
  let dict = {};
  obj.forEach(function (objResults) {
    if (objResults.completed === true ) {
      let id = objResults.userId;
      if ((id in dict) === false) {
        dict.id = 0;
      }
      dict.id += 1;
    }
  }); 
  console.log(dict);
});
