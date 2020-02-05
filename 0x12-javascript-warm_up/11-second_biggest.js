#!/usr/bin/node
function secondMax (a, b) {
  return (a - b);
}
if (process.argv.length < 4) {
  console.log(0);
} else {
  let x = process.argv.slice(2);
  x.sort(secondMax);
  console.log(x[x.length - 2]);
}
