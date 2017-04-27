#!/usr/bin/python3

from turtle import *

def koch(degree, canvas_width):
	arm_length = canvas_width/3
	if degree == 1:
		forward(arm_length)
		left(60)
		forward(arm_length)
		right(120)
		forward(arm_length)
		left(60)
		forward(arm_length)
	else:
		koch(degree-1, arm_length)
		left(60)
		koch(degree-1, arm_length)
		right(120)
		koch(degree-1, arm_length)
		left(60)
		koch(degree-1, arm_length)

def center_align_drawing(canvas_width):
	# Moving turtle to appropriate position
	# to make the whole drawing center aligned
	penup()
	goto(-(canvas_width/2),-100)
	pendown()

def pre_drawing_tasks(canvas_width):
	# to speed up drawing
	tracer(0, 0)
	speed(0)
	center_align_drawing(canvas_width)

def post_drawing_tasks():
	# Updating drawing buffer to display after drawing is complete.
	# This is required as screen updation was turned off in
	# setup method to speedup drawing
	update()

	# Preventing program termination right after completing drawing.
	# This gives user time to appriciate the beauty of drawing.
	exitonclick()

def main():
	# Obtaining user inputs
	# 	n - Degree of kock curve
	# 	l - total width of curve
	degree = int(input('Degree of curve: '))
	canvas_width = int(input('Width of canvas: '))
	pre_drawing_tasks(canvas_width)
	koch(degree, canvas_width)
	post_drawing_tasks()

if __name__ == '__main__':
	main()
