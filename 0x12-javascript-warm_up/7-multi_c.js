#!/usr/bin/node
let myString = 'C is fun\n';
if (process.argv.length === 2) {
  console.log('Missing number of occurrences')
} else {
  console.log(myString.repeat(process.argv[2]))
}
