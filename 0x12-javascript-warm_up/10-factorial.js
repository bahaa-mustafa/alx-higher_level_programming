#!/usr/bin/node
function factorial (a) {
  if (a === 1 || a === 0 || a < 0) {
    return (1);
  }
  return (a * factorial(a - 1));
}
if (isNaN(process.argv[2])) { console.log(1); } else {
  console.log(factorial(parseInt(process.argv[2])));
}
