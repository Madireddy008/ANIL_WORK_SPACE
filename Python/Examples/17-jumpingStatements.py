'''
Control Statements:
    1. conditional Statements
        if
        else
        elif
        nested if
    2. Looping STatement
        for
        while
        nested loop
    3. Jumping Statement
        pass--> Ignore
        continue--> skip current iteration
        break--> Terminate
'''
print ('Example for Pass')
if True:
    pass

print ('Example for Break')
a='Python'
for i in a:
    if i=='n':
        break
    print(i)
    
print ('Example for Continue')
b='PythonLife'
for j in b:
    if j=='n':
        continue
    print(j)