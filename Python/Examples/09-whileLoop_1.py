# break the loop as soon it sees 'e' or 's' 
i = 0
a = 'geeksforgeeks'

while i < len(a): 
	if a[i] == 'e' or a[i] == 's': 
		i += 1
		break
		
	print('Current Letter :', a[i]) 
	i += 1

