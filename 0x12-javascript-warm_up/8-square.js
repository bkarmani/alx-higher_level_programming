#!/usr/bin/node
const [, , arg1] = process.argv;
let count = 0;
let boxObj = '';
if (~~arg1 === 0) {
  console.log('Missing size');
} else {
  count = parseInt(arg1);
}
for (let i = 0; i < count; i++) {
  boxObj = boxObj + 'X';
}
for (let i = 0; i < count; i++) {
  console.log(boxObj);
}
