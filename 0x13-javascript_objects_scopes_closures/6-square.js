#!/usr/bin/node
const SquareP = require('./5-rectangle');

class Square extends SquareP {
  charPrint (c) {
    let charP = 'X';
    if (typeof(c != 'undefined')) {
      charP = c;
    }
    const arrayI = [];
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
	array[j] = charP;
      }
      console.log(arrayI.join(''));
    }
  }
}

module.exports = Square;
