# Variables

i = 2
j = 3
k = 5

console.log i, j, k

x = 0.5
y = 1.27
pi = 3.146

console.log x, y, pi

circumference_1 = pi * y
circumference_2 = pi * n

console.log circumference_1, circumference_2

#Operators
m = 2 * 3
n = 3 + 5

console.log m, n

average = (i + j + k) / 3

console.log average

a = 3
b = 8.6
c = 2.12

discriminant = Math.sqrt b * b - 4 * a * c
denominator = 2 * a
x1 = (-b + discriminant) / denominator
x2 = (-b - discriminant) / denominator

console.log x1, x2

a = "Hello, world"
c = "This is" + " more text"

console.log a, c

console.log a.length, c.length


# Control flow

MIN_BALANCE = 25

current_balance = 30
transaction_amount = 10

if (current_balance - transaction_amount) < MIN_BALANCE
	console.log "This transaction is too large."
else
	current_balance -= transaction_amount
console.log "Your current balance is: $" + current_balance

i = 0
while i < 10
	console.log i
	i++

console.log i for i in [0..10]
console.log i for i in [0...10]
