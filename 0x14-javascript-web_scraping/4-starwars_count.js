#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const objResults = JSON.parse(body).results;
  let role = 0;
  objResults.forEach(function (cast) {
    cast.characters.forEach(function (character) {
      if (character === 'https://swapi-api.hbtn.io/api/people/18/') {
        role++;
      }
    });
  });
  console.log(role);
});
