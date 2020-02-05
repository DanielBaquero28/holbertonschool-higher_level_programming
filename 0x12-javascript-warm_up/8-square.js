#!/usr/bin/node
const myString = 'X';
if (parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(myString.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}
