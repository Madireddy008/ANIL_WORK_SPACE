#TUPLE IN PYTHON
t=(1,2,3,1.1,2.3,3.4,True,"Anil")
t1=(1,2,3,4,5,6)
t2=(7,8,9)
print("printing type of t =",t,":" ,type(t))

#INDEXING IN TUPLE
print("Printing Indexing in tuple t =",t,":",t[5])

#SLICING IN TUPLE
print("Printing Slicing in tuple t =",t,":",t[0:7:2])

#BUILTIN METHODS IN TUPLE
print("Printing Minimum in tuple t1 =",t1,":",min(t1))
print("Printing Maximum in tuple t1 =",t1,":",max(t1))
print("Printing Sum in tuple t1 =",t1,":",sum(t1))
print("Printing Length in tuple t1 =",t1,":",len(t1))
print("Printing Length in tuple t =",t,":",len(t))

#CONCATINATION IN TUPLE
print("Printing addition of Tuples t1 =",t1,"and","t2 =",t2,":",t1+t2)

#REPETITION IN TUPLE
print("Printing Repetition of Tuples t2 =",t2,":",t2*2)

#MEMBERSHIP OPERATIONS
print("Is 1 in t1 =",t1,"?:",1 in t1)
print("Is 1 in t1 =",t1,"?:",1 not in t1)
print("Is t2 =",t2, "is t1 =",t1,"?:",t2 is t1)
print("Is t2 =",t2, "is not t1 =",t1,"?:",t2 is not t1)

#ITERATION IN TUPLE
for i in t:
    print(i)