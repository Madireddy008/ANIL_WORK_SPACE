'''
i = 1
while i <= 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 7:
    continue
  i += 1
  '''
   
# Prints all letters except 'e' and 's' 
i = 0
a = 'geeksforgeeks'
print(len(a))

while i < len(a): 
    if a[i] == 'e' or a[i] == 's': 
        i += 1
        continue
          
    print('Current Letter :', a[i]) 
    i += 1
