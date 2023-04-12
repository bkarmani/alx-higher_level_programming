#!/usr/bin/node
const [, , arg1] = process.argv;
let count = 0;
if (~~arg1 === 0) {
  console.log('Missing number of occurrences');
} else {
  count = parseInt(arg1);
}
for (let i = 0; i < count; i++) {
  console.log('C is fun');
}
