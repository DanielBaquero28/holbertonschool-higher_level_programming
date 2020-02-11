#!/usr/bin/node
const request = require('request');

const targetURL = 'https://swapi.co/api/people/18/';
let counter = 0;
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body)
    const results = content.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results.characters;
      for (let j = 0; j < characters.length; j++) {
        if (['results'][i].characters[j] === targetURL) {
          counter++;
        }
      }
    }
  }
  console.log(counter);
});
