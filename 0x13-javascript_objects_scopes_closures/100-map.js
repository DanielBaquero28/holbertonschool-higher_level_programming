#!/usr/bin/node
const list = require('./100-data').list;

const newArray = list.map(function (n, index) {
  return (n * index);
});

console.log(list);
console.log(newArray);
