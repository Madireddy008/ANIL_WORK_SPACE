#LIST IN PYTHON
l=[1,2,3,True,'Anil',1.111,2.3,3.0]
print("Printing type of l=[1,2,3,True,'Anil',1.1,2.3]:",type(l))

#INDEXING
print("Farward Indexing of list l[3]:", l[3])
print("Backward Indexing of list l[-1]:", l[-1])
print("Farward Indexing of list l[4]:", l[4])

#SLICING
print("Slicing in List l[0:5:2]:", l[0:5:2])
print("Slicing in List l[0:6:3]:", l[0:7:3])

#APPENDING LIST
l.append("Kumar")
print("Appending Some Data into l.append('Kumar'):",l)

#EXTENDING LIST
l.extend([5.5,6.0,False])
print("Extending Some Data into list l l.extend([5.5,6.0,False]):",l)

#COUNT IN LIST
print("Count of 1 in List l:",l.count(1))

#REMOVING DATA IN LIST
l.remove(1)
print("Removing 1 from list l :",l)

#POP IN LIST
l.pop(-1)
print("Poping index -1 from list l :",l)

#INDEX IN LIST
print("indexing of list value False:",l.index(6.0))

#INSERT IN LIST
l.insert(0,'xyz')
print("Inserting some data into List l:",l)

#LOOPING IN LIST
for i in l:
    print(i)

