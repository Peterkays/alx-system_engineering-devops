#!/usr/bin/node
const request = require('request');
const args = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${args}`;
request(url, function (error, response, body) {
  if (!error) {
    for (const character of JSON.parse(body).characters) {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});