#!/usr/bin/node

const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) {
    console.error(err);
  } else {
    const object = JSON.parse(body);
    console.log(object.title);
  }
});
