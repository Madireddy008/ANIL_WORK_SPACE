#for integer as input

list_of_numbers = []

n = int(input("enter the elements:"))

for i in range(0, n):
    ele = int(input("Enter integer value:"))
    list_of_numbers.append(ele)
print(list_of_numbers)

print(list_of_numbers[-1] + list_of_numbers[2])



#for string as input
'''

list_of_numbers = []

n = int(input("enter the string elements elements:"))

for i in range(0, n):
    ele = str(input())
    list_of_numbers.append(ele)
print(list_of_numbers)


'''

#for input as list of list
'''
#Get a list as input from user in Python List of lists as input 
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = [input("enter str value:"), int(input("enter int value:"))]
	lst.append(ele)

print(lst)

'''