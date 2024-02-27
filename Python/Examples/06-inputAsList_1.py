# creating an empty list
list = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range n elements
for i in range(0, n):
	ele = int(input())
	# adding the element
	list.append(ele) 

#for loop for finding positive and negative number in the given list of numbers
for j in list:
    if j > 0:
        print(j, "is positive number")
    elif j < 0:
        print(j, "is negative number") 
    else:
        print(j, "is whole number")

#for loop for finding positive and negative number in the given list of numbers
for m in list:
    if m%2 == 0:
        print(m, "is even number")
    else:
        print(m,"is odd number")


         



