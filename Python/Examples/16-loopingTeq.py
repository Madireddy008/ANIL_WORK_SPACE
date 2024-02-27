'''
Python supports various looping techniques by certain inbuilt functions, in various sequential containers. These methods are primarily very useful in competitive programming and also in various projects that require a specific technique with loops maintaining the overall structure of code.  A lot of time and memory space is been saved as there is no need to declare the extra variables which we declare in the traditional approach of loops.

Where they are used?
Different looping techniques are primarily useful in places where we don’t need to actually manipulate the structure and order of the overall containers, rather only print the elements for a single-use instance, no in-place change occurs in the container. This can also be used in instances to save time.

Different looping techniques using Python data structures  are: 
Way 1: Using enumerate():  enumerate() is used to loop through the containers printing the index number along with the value present in that particular index.

'''

# python code to demonstrate working of enumerate()

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
	print(key, value)



# python code to demonstrate working of enumerate()

for key, value in enumerate(['Geeks', 'for', 'Geeks','is', 'the', 'Best','Coding', 'Platform']):
	print(value, end=' ')
