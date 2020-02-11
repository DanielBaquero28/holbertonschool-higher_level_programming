#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const requestURL = process.argv[2];

request(requestURL, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const content = body;
    fs.writeFile(process.argv[3], content, 'utf-8', (errorSec) => {
      if (errorSec) {
	console.log(errorSec);
      }
    });
  }
});
