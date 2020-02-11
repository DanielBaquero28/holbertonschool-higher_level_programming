#!/usr/bin/node
let data = require('./101-data').dict;
const dictO= {}
for (const key in data) {
  if (dictO[data[key]] == undefined) {
    dictO[data[key]] = [];
  }
  dictO[data[key]].push(key);
}
console.log(dictO);
