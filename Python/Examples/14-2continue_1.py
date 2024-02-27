'''

Continue with Nested loops
In this example, we are creating a 2d list that includes the numbers from 1 to 9 and we are traversing in the list with the help of two for loops and we are skipping the print statement when the value is 3.

'''

# prints all the elements in the nested list 
# except for the ones with value 3
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in nested_list:
	for j in i:
		if j == 3:
			continue
		print(j)
