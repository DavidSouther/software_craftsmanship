// Variables

var i = 2;
var j = 3;
var k = 5;

console.log(i, j, k);

var x = 0.5;
var y = 1.27;
var pi = 3.146;

console.log(x, y, pi);

var circumference_1 = pi * y;
var circumference_2 = pi * n;

console.log(circumference_1, circumference_2);

//Operators

var m = 2 * 3;
var n = 3 + 5;

console.log(m, n);

var average = (i + j + k) / 3;
var average_2 = (i + j + k) / 3.0;

console.log(average, average_2);

var a = "Hello, world";
var b = 'Hello, world';
var c = "This is" + " more text";

console.log(a, b, c);

console.log(a.length, b.length, c.length);

console.log(a.substring(4), b.substring(-4), c.substring(2, 9));

var MIN_BALANCE = 25;
var current_balance = 30;
var transaction_amount = 10;

if( (current_balance - transaction_amount) < MIN_BALANCE)
{
	console.log("This transaction is too large.");
}
else
{
	current_balance -= transaction_amount;
}
console.log("Your current balance is: $" + current_balance);

for(i=0; i<10; i++)
{
	console.log(i);
}
