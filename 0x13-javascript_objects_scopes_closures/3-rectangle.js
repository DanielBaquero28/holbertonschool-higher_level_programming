#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    const array = [];
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
	array[j] = 'X';
      }
      console.log(array.join(''));
    }
  }
}
module.exports = Rectangle;
