#!/usr/bin/node
let myString = 'C is fun';
if (parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(myString);
  }
} else {
     console.log('Missing number of occurrences')
}
