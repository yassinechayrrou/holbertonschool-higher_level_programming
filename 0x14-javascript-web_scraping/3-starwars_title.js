#!/usr/bin/node

const request = require('request');
const ep = parseInt(process.argv[2]);
const URL = 'https://swapi-api.hbtn.io/api/films/' + ep;
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
