'''
Continue with While Loop
In this example, we are using a while loop which traverses till 9 if i = 5 then skip the printing of numbers.

'''

# prints the numbers between
# 0 and 9 that are not equal to 5
i = 0
while i < 10:
	if i == 5:
		i += 1
		continue
	print(i)
	i += 1
