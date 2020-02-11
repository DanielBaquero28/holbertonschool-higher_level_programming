#!/usr/bin/node
const file = require('file');

const firstFile = file.readFileSync(process.argv[2]).toString();
const secondFile = file.readFileSync(process.argv[3]).toString();
file.writeFileSync(process.argv[4], firstFile + secondFile);
