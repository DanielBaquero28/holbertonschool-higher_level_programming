#!/usr/bin/node
if (parseInt(process.argv[2])) {
  console.log(factorial(parseInt(process.argv[2])));
} else {
  console.log(1);
}
function factorial (x) {
  if (x == 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
