#!/usr/bin/node
const request = require('request');

const requestURL = process.argv[2];
request(requestURL, function (error, response, body) {
  const targetSub = /18/;
  let counter = 0;
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const resultsList = content.results;
    for (const i of resultsList) {
      const charactersList = i.characters;
      for (const j of charactersList) {
        if (targetSub.test(charactersList[j]) === true) {
          counter++;
        }
      }
    }
  }
  console.log(counter);
});
