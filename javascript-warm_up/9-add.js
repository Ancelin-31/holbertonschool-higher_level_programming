#!/usr/bin/node

const firstNumber = Number(process.argv[2]);
const secondNumber = Number(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(firstNumber, secondNumber);
