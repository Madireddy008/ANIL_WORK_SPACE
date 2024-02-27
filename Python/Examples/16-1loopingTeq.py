'''

Way 2: Using zip(): zip() is used to combine 2 or more containers printing the values sequentially. The loop exists only till the smaller container ends. A detailed explanation of zip() and enumerate() can be found here.

Example 1: Two different data type(list,tuple)

'''

# python code to demonstrate working of zip()

names = ['Deep', 'Sachin', 'Simran']	 # list
ages = (24, 27, 25)		 # tuple

for name, age in zip(names, ages):
	print('Name: ', name)
	print('Age: ', age)
	print()