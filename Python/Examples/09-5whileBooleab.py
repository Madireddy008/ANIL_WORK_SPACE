'''
While loop with Boolean values
One common use of boolean values in while loops are to create an infinite loop that can only be exited based on some condition within the loop. 

Example:

In this example, we initialize a counter and then use an infinite while loop (True is always true) to increment the counter and print its value. We check if the counter has reached a certain value and if so, we exit the loop using the break statement.

'''

# Initialize a counter 
count = 0

# Loop infinitely 
while True: 
	# Increment the counter 
	count += 1
	print(f"Count is {count}") 

	# Check if the counter has reached a certain value 
	if count == 10: 
		# If so, exit the loop 
		break

# This will be executed after the loop exits 
print("The loop has ended.") 
