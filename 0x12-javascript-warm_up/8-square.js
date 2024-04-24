#!/usr/bin/node
if ((parseInt(process.argv[2])) > 0) {
  let i = 0; let t = 0;
  for (i; i < parseInt(process.argv[2]); i++) {
    for (t = 0; t < parseInt(process.argv[2]); t++) {
      console.log('x'.endsWith(''));
    }
    console.log('\n');
  }
} else {
  console.log('Missing size');
}
