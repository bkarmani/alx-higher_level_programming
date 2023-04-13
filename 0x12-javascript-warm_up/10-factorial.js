#!/usr/bin/node
const [, , arg1] = process.argv;
function facto (n) {
  let factorial = 1;
  if (n < 0) {
    return -1;
  } else {
    for (let num = 2; num <= n; num++) {
      factorial = factorial * num;
    }
  }
  return factorial;
}
const arg = facto(parseInt(arg1));
console.log(arg);
