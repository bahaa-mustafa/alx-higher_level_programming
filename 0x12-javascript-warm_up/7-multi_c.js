#!/usr/bin/node
if ((parseInt(process.argv[2]))) {
  let i = 0;
  for (i; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
