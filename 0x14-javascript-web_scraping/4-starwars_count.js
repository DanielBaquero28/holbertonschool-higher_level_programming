#!/usr/bin/node
const request = require('request');

const targetSub = /18/;
let counter = 0;
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body)
    const results = content.results;
    for (const i of results) {
      const characters = i.characters;
      for (const j of characters) {
        if (targetSub.test(characters[j])=== true) {
          counter++;
        }
      }
    }
  }
  console.log(counter);
});
