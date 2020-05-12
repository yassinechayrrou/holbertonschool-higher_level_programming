#!/usr/bin/node

const request = require('request');
let object;

request.get('https://swapi-api.hbtn.io/api/films/' + parseInt(process.argv[2]), function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    object = JSON.parse(body);
    if (object.title === undefined) {
      process.stdout.write('');
    } else {
      console.log(object.title);
    }
  }
});
