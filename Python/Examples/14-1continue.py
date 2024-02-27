'''
Printing range with Python Continue Statement
Consider the situation when you need to write a program that prints the number from 1 to 10, but not 6. 

It is specified that you have to do this using a loop and only one loop is allowed to use. Here comes the usage of the continue statement. What we can do here is we can run a loop from 1 to 10 and every time we have to compare the value of the loop variable with 6. If it is equal to 6 we will use the continue statement to continue to the next iteration without printing anything, otherwise, we will print the value.

'''

# loop from 1 to 10
for i in range(0, 11):

	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 6:
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end=" ")
