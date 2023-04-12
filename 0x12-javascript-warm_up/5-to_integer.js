#!/usr/bin/node
const [, , arg1] = process.argv;
if (~~arg1 === 0) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(arg1));
}
