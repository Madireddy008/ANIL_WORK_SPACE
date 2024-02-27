# Prints all letters except 'e' and 's' 
i = 0
a = 'geeksforgeeks'
  
while i < len(a): 
    if a[i] == 'e' or a[i] == 's': 
        i += 1
        continue
          
    print('Current Letter :', a[i]) 
    i += 1


# Python program to illustrate 
# while loop 
count = 0
while (count < 3): 
	count = count + 1
	print("Hello Geek")