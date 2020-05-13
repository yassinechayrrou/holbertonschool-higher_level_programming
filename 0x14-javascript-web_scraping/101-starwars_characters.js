#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(URL, (err, res, body) => {
  if (err) { return console.log(err); }
  const charactersURL = JSON.parse(body).characters;
  recurr(charactersURL, 0);
});

function recurr(characters, idx) {
  for (let i = 0; i < )
  characters.forEach(character => {
    request(character, (err, res, body) => {
      if (err) { return console.log(err); }
      console.log(JSON.parse(body).name);
      if ( idx + 1 < character.length) {
        recurr(character, idx + 1);
      }
    });
  });
}
