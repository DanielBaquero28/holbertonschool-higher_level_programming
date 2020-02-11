#!/usr/bin/node
const file = require('fs');

file.readFileSync(process.argv[2], 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  }
  console.log(data.toString());
});
