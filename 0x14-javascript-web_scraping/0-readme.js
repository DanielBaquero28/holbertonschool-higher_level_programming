#!/usr/bin/node
const file = require('fs');

const content;
file.readFile(process.argv[2], function (error, data) {
  if (error) {
    throw error;
  }
  content = data;

  processFile();
});

function processFile() {
  console.log(content);
}
