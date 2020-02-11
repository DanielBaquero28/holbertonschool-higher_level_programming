#!/usr/bin/node
const request = require('request');

const requestURL = `http://swapi.co/api/films/${process.argv[2]}`;
request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
