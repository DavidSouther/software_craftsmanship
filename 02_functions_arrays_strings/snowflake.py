from colorsys import hls_to_rgb
from turtle import *

def reset():
	goto(-250, 0)
	clear()

def poscolor(pos):
	distance = pos[0] * pos[0] + pos[1] * pos[1]
	hue = (distance % 255) / 255
	rgb = hls_to_rgb(hue, 0.5, 0.5)
	return rgb

def snowflake(length, order):
	if order == 0:
		color(poscolor(pos))
		forward(length)
	else:
		snowflake(length / 3, order - 1)
		left(60)
		snowflake(length / 3, order - 1)
		right(120)
		snowflake(length / 3, order - 1)
		left(60)
		snowflake(length / 3, order - 1)

# To understand recursion:
# Unroll the loop
def snowflake_0(length):
	color(poscolor(pos()))
	forward(length)

def snowflake_1(length):
	snowflake_0(length / 3)
	left(60)
	snowflake_0(length / 3)
	right(120)
	snowflake_0(length / 3)
	left(60)
	snowflake_0(length / 3)

def snowflake_2(length):
	snowflake_1(length / 3)
	left(60)
	snowflake_1(length / 3)
	right(120)
	snowflake_1(length / 3)
	left(60)
	snowflake_1(length / 3)

def snowflake_3(length):
	snowflake_2(length / 3)
	left(60)
	snowflake_2(length / 3)
	right(120)
	snowflake_2(length / 3)
	left(60)
	snowflake_2(length / 3)


# snowflake = curve with angle in [60, -120, 60, 0]
def snowflakeShort(length, order):
	if order == 0:
		color(poscolor(pos()))
		forward(length)
	else:
		for angle in [60, -120, 60, 0]:
			# left(-120) = right(120)
			# Last 0 to get all four lines
			snowflake(length / 3, order - 1)
			left(angle)

def curve(length, order):
	if order == 0:
		color(poscolor(pos()))
		forward(length)
	else:
		for angle in [60, -120, 60, 0]:
			curve(length / 3, order -1)
			left(angle)

if __name__ == '__main__':
	speed(0)
	for i in range(0, 5):
		reset()
		curve(500, i)
		raw_input("Press enter to continue...")
