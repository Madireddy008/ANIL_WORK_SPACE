'''
Tuple:
    -()
    -allow different type of elements
    -allow duplicates
    -allows index and slicing
    -it is Immutable (cannot changeble)
    -it contain no methods
    -we need to use builtin methods
Syntax:
    t1=(1,2,3,4,5,"6.ANIL","7.kumar",False)
    t2=(10,11,12)
Operations:
    -concatination
        print (t1+t2)
    -iteration
    -membership operations
    -identity operations
    -repetation
'''
tuple=(1,11,111,2,22,222)
t1=(1,2,3)
t2=(4,5,6)
print ('tuples declared are below')
print ('tuple=(1,11,111,2,22,222) && t1=(1,2,3) && t2=(4,5,6)')
#printing tupletype
print('printing tupletype')
print (type(tuple))
#slicing tuple
print('printing tupleslicing')
print(tuple[0:7:2])
#printing minimum number in tuple
print('printing minimum number in tuple')
print (min(tuple))
#printing maximum number in tuple
print('printing maximum number in tuple')
print (max(tuple))
#printing sum in tuple
print('printing sum in tuple')
print (sum(tuple))
#printing len tuple
print('printing len tuple')
print (len(tuple))
#printing concatination of tuple
print('printing concatination of tuple')
print (t1+t2)
#printing repetation od tuple
print ('printing repetition in tuple')
print (t1*2)
#printing iteration in tuple
print ('printing iteration in tuple')
for i in tuple:
    print (i)
#printing membership in tuple
print ('printing membership in tuple')
print ('is 1 in tuple ??')
print (1 in tuple)
print ('is 222 in tuple ??')
print (222 in tuple)
print ('is 3 in t1 ??')
print (3 in t1)
print ('is 5 in t2 ??')
print (5 in t2)
print ('is 15 in t2 ??')
print (15 in t2)
print ('is 15 not in t2 ??')
print (15 not in t2)
print ('is t1=t2 ??')
print (t1 is t2)
print ('is t1 is not t2 ??')
print (t1 is not t2)