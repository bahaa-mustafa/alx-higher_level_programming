#!/usr/bin/node
function factorial (a) {
  let result = 1;
  if (isNaN(a)) {
    console.log(result);
  } else {
    for (let i = parseInt(a); i > 0; i--) {
      result *= i;
    }
    console.log(result);
  }
}
const a = process.argv[2];
factorial(a);
