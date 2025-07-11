#!/usr/bin/node

const size = Number(process.argv[2]);
const printSymbol = 'X';

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log((printSymbol).repeat(size));
  }
} else {
  console.log('Missing size');
}
