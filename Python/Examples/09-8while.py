'''
Python While Loop Exercise Questions
Below are two exercise questions on Python while loop. We have covered 2 important exercise questions based on the bouncing ball program and the countdown program.

Q1. While loop exercise question based on bouncing ball problem

'''

initial_height = 10
bounce_factor = 0.5
height = initial_height 
while height > 0.1: 
	print("The ball is at a height of", height, "meters.") 
	height *= bounce_factor 
print("The ball has stopped bouncing.")
