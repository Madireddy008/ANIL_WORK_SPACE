'''
Task 6: Identity and Membership Operators
Create a list my_list containing a few elements.
Use identity operators (is and is not) to check if two variables are the same object.
Use membership operators (in and not in) to check if an element is present in my_list.
Print the results.

'''

my_list = [1, 2, 3.5, 'Anil', 'Sravani', 'Moviya']
my_list1 = [1, 2, 3.5, 'Anil', 'Sravani', 'Moviya']
my_list2 = [1, 2, 3.5, 'Kumar', 'Madireddy', 'Moviyasri']

print(my_list is my_list1)
print(my_list is not my_list1)
print('Anil' in my_list)
print('Madireddy' not in my_list2)
