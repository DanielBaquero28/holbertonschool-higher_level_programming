#!/usr/bin/node
const request = require('request');

const requestURL = process.argv[2];
request(requestURL, function (error, response, body) {
  if (error == null) {
    const idTasksC = {};
    const content = JSON.parse(body);
    for (let i = 0; i < content.length; i++) {
      if (content[i].completed === true) {
        if (idTasksC[content[i].userId] === undefined) {
          idTasksC[content[i].userId] = 0;
        }
        idTasksC[content[i].userId]++;
      }
    }
    console.log(idTasksC);
  }
});
