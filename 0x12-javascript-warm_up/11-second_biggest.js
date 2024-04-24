#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  process.argv.sort((a, b) => b - a);
  console.log(process.argv[3]);
}
