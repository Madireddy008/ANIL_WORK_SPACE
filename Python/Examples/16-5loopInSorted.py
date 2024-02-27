# python code to demonstrate working of sorted()

# initializing list
lis = [1, 3, 5, 6, 2, 1, 3]

# using sorted() to print the list in sorted order
print("The list in sorted order is : ")
for i in sorted(lis):
	print(i, end=" ")

print("\r")

# using sorted() and set() to print the list in sorted order
# use of set() removes duplicates.
print("The list in sorted order (without duplicates) is : ")
for i in sorted(set(lis)):
	print(i, end=" ")
