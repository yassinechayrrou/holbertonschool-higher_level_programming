#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
request(URL, function (err, res, body) {
  if (err != null) {
    return console.log(err);
  }
  const objResults = JSON.parse(body).results;
  let role = 0;
  objResults.forEach(function (cast) {
    cast.characters.forEach(function (character) {
      const splitChar = character.split('/');
      const len = splitChar.length;
      if (splitChar[len - 2] === '18') {
        role++;
      }
    });
  });
  console.log(role);
});
