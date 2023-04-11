#!/usr/bin/node
const response1 = 'No argument';
const response2 = 'Argument found';
const response3 = 'Arguments found';
const args = process.argv;
if (args.length === 2) {
  console.log(response1);
} else if (args.length === 3) {
  console.log(response2);
} else {
  console.log(response3);
}
