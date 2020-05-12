#!/usr/bin/node

const request = require('request');
const ep = parseInt(process.argv[2]);
let object;
if (ep < 8) {
  const URL = 'https://swapi-api.hbtn.io/api/films/' + ep;
  request.get(URL, function (err, res, body) {
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
}
