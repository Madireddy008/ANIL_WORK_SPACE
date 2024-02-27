# python code to demonstrate working of sorted()

# initializing list
basket = ['guave', 'orange', 'apple', 'pear','guava', 'banana', 'grape']

# using sorted() and set() to print the list
# in sorted order
for fruit in sorted(set(basket)):
	print(fruit)
