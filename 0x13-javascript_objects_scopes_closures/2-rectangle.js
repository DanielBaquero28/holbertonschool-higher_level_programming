#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    (w <= 0 || h <= 0) ? Rectangle(): Rectangle(w, h);
  }
}
module.exports = Rectangle;
