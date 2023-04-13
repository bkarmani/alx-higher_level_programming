#!/usr/bin/node
const [, , arg1, arg2] = process.argv;
function add (a, b) {
  const arg1 = parseInt(a);
  const arg2 = parseInt(b);
  return arg1 + arg2;
}
const outPut = add(arg1, arg2);
console.log(outPut);
