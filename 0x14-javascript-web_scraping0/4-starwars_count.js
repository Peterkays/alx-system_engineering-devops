#!/usr/bin/node
const request = require('request');
const args = process.argv[2];
const url = args;
request(url, function (error, response, body) {
  let n = 0;
  if (!error && response.statusCode === 200) {
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.split('18').length === 2) {
          n++;
        }
      }
    }
  }
  console.log(n);
});