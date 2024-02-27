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
#defining Variable

#for loop printing
print ("Examples of for loop")
a=[1,2,3,4,5]
b= 'Python'
c=[12345]
print ("printing a")
for i in a:
    print(i)
print ("printing b")
for j in b:
    print(j)
print ("printing c")
for k in c:
    print(k)
 
#tables 1 to 20 using for loop    
for x in range(1,21):
    for y in range(1,11):
        print (x*y)

#while loop Printing
print ("Examples of While loop")
d=10
while d<20:
    d+=1
    print ("NO")
    