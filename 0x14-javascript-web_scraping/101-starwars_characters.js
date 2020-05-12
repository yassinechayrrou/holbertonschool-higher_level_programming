#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const films = JSON.parse(body).results;
  films.forEach(function (episode) {
    if (episode.episode_id === parseInt(movieId)) {
      episode.characters.forEach(function (character) {
        request(character, function (err, res, body) {
          if (err) {
            return console.log(err);
          }
          console.log(JSON.parse(body).name);
        });
      });
    }
  });
});
