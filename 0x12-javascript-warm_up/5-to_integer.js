#!/usr/bin/node
const [, , arg1] = process.argv;
if (~~arg1 === 0) {
  console.log('not a number');
} else {
  console.log('number:', parseInt(arg1));
}
