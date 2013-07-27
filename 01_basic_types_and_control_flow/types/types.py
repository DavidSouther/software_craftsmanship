#!/usr/bin/env python

print "Hello, world"

print 'Hello, again'

print 2, 3, 5, 7, 11

print 0.5, 1.27, 3.146

print 'h', 'e', 'l', 'l', 'o'

i = 2
j = 3
k = 5

print i, j, k

m = 2 * 3
n = 3 + 5

print m, n

x = 0.5
y = 1.27
pi = 3.146

print x, y, pi

circumference_1 = pi * y
circumference_2 = pi * n

print circumference_1, circumference_2

average = (i + j + k) / 3
average_2 = (i + j + k) / 3.0

print average, average_2

a = "Hello, world"
b = 'Hello, world'
c = "This is" + " more text"

print a, b, c

#print a.length, b.length, c.length

#print a.substring(4), b.substring(-4), c.substring(2, 9)

MIN_BALANCE = 25
current_balance = 30
transaction_amount = 10

if( (current_balance - transaction_amount) < MIN_BALANCE):
	print "This transaction is too large."
else:
	current_balance -= transaction_amount
print "Your current balance is: $" + str(current_balance)

for i=0; i < 10; i++:
	print i;
