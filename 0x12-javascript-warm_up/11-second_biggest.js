#!/usr/bin/node
const array = process.argv.slice(2).map(Number);
const argLen = process.argv.length;
if (argLen <= 3) {
  console.log('0');
} else {
  const secH = array.sort(function (a, b) { return b - a; })[1];
  console.log(secH);
}
