#!/usr/bin/node
const request = require('request');
const args = process.argv[2];
request(args, function (error, response, body) {
  if (!error) {
    console.log('code:', response.statusCode);
  }
});