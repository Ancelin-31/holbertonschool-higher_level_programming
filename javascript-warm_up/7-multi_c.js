#!/usr/bin/node

const x = Number(process.argv[2]);
const string = 'C is fun';

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log(string);
  }
} else {
  console.log('Missing number of occurrences');
}
