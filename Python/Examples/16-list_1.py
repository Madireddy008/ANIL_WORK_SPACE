'''
List:
    -[]
    -Mutable Data Type
    -Allows Duplicates :
        ex: a=[1,1,1,1]
    -Stores Different types of elemrnts:
        Ex: a=[1,2.2,'ANIL KUMAR']
    -allows Indexing:       
        bkd indexing  -3 -2       -1  
                EX: a=[1,2.2,'ANIL KUMAR']
        fwd indexing   0  1       2
                
                Ex: a[0] is 1 in above
                    a[-1] is ANIL KUMAR
                    a[1] is 2.2
'''
a=[1,2.2,'Anil Reddy',2,4,5]
print (a)
print ('printing using indexing')
print ('print index 0 of variable a')
print (a[0])
print ('print index 1 of variable a')
print (a[1])
print ('print index 2 of variable a')
print (a[2])
print ('print index -1 of variable a')
print (a[-1])
print ('print index -2 of variable a')
print (a[-2])
print ('print index -3 of variable a')
print (a[-3])
print ('printing using slicing')
#prints index from 0 to 4 by skipping alternative index
print (a[0:4:2])

'''
append --> adds in last line of string
extend --> adds bulk data into the list
remove --> removes with list value
pop    --> removes with index number
count  --> counts the given list's value
index  --> shows the index number of list's value
insert --> inserts the values in the given index number place
'''
a.append("Madireddy")
print (a)
a.extend([1.0,2.0,"kumar"])
print(a)
print (a.count(1))
print(a)
a.remove(2)
print (a)
a.pop(-1)
print (a)
a.pop(-2)
print (a)
print (a.index('Anil Reddy'))
print (a)
for i in a:
    print (i)
a.insert(2,100)
print(a)