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
        pass
        continue
        break
'''




#Simple If condition
print ("Output for IF=TRUE")
if True:
    print ("I am IF")
else:
    print ("I am else")


    
#Simple Else Condition
print ("Output for IF=FALSE")
if False:
    print ("I am IF")
else:
    print ("I am else")




#Simple ELIF Conditions
print ("Output for ELIF=TRUE")
if False:
    print ("I am IF")
elif True:
    print ('I am ELIF')
else:
    print ("I am ELSE")




#Simple ELIF Conditions
print ("Output for ELIF-ELSE=TRUE")
if False:
    print ("I am IF")
elif False:
    print ('I am ELIF')
else:
    print ("I am ELSE")



#Simple Nested If Conditions
print ('Nested If Conditions')
if True:
    print ("Outer IF")
    if True:
        print ("Inner IF")
    else:
        print ("Inner ELSE")
else:
    print ("Outer ELSE")




#Simple Nested If Conditions-2  
print ('Nested If Conditions-2')
if False:
    print ("Outer IF")
    if True:
        print ("Inner IF")
    else:
        print ("Inner ELSE")
else:
    print ("Outer ELSE")




#Simple Nested If Conditions-3
print ('Nested If Conditions-3')
if True:
    print ("Outer IF")
    if False:
        print ("Inner IF")
    else:
        print ("Inner ELSE")
else:
    print ("Outer ELSE")
    



#Simple Nested If Conditions-4
print ('Nested If Conditions-4')
if False:
    print ("Outer IF")
    if False:
        print ("Inner IF")
    else:
        print ("Inner ELSE")
else:
    print ("Outer ELSE")




#1. conditional Statements
'''
Syntax:
    if condition:
        statement
    else:
        statement
'''
print ("1. conditional Statements with if else")
a=36
if a>18:
    print ("You Can Vote")
else:
    print ("You Cannot Vote")

'''
Syntax:
    if Condition:
        Statement
    elif Condition:
        Statement
    else:
        Statement
'''
print ("1.1 conditional Statements with elif")
b=18
if b>18:
    print ("You Can Vote")
elif b==18:
    print ("You Can Vote")
else:
    print ("You Cannot Vote")
    
    
print ("1.2 conditional Statements with elif and")
c=18
if c>18 or c==18:
    print ("You Can Vote")
else:
    print ("You Cannot Vote")
    
    
print ("1.3 conditional Statements with elif")
d=15
if d>18:
    print ("You Can Vote")
elif d==18:
    print ("You Can Vote")
else:
    print ("You Cannot Vote")
    
    
print ("1.4 conditional Statements with elif and")
e=17
if e>18 or e==18:
    print ("You Can Vote")
else:
    print ("You Cannot Vote")

