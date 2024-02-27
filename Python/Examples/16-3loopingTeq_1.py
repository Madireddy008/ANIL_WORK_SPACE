# python code to demonstrate working of items()

d = {"geeks": "for", "only": "geeks"}

# iteritems() is renamed to items() in python3
# using items to print the dictionary key-value pair
print("The key value pair using items is : ")
for i, j in d.items():
	print(i, j)
