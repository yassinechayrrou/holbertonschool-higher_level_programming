#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const obj = JSON.parse(body).characters;
  obj.forEach(function (character) {
    request(character, function (err, res, body) {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
