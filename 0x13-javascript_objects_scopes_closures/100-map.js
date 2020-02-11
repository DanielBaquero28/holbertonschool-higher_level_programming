#!/usr/bin/node
const Map = require('./100-data').list;

for (let i = 0; i < list.length; i++) {
  const newArray = list.map(x => x * i);
}

console.log(list);
console.log(newArray);
