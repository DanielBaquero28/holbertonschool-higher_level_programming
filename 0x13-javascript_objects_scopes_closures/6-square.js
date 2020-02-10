#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    let charP = 'X';
    if (c) {
      charP = c;
    }
    const arrayI = [];
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
	arrayI[j] = charP;
      }
      console.log(arrayI.join(''));
    }
  }
}

module.exports = Square;
