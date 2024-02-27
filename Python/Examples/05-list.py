tuple=(1,11,111,2,22,222)
t1=(1,2,3)
t2=(4,5,6)
print ('tuples declared are below')
print ('tuple=(1,11,111,2,22,222) && t1=(1,2,3) && t2=(4,5,6)')
#printing tupletype
print('printing tupletype::',type(tuple))

#slicing tuple
print('printing tupleslicing::',tuple[0:7:2])

#printing minimum number in tuple
print('printing minimum number in tuple::',min(tuple))

#printing maximum number in tuple
print('printing maximum number in tuple::',max(tuple))

#printing sum in tuple
print('printing sum in tuple::',sum(tuple))

#printing len tuple
print('printing len tuple::',len(tuple))

#printing concatination of tuple
print('printing concatination of tuple::',t1+t2)

#printing repetation od tuple
print ('printing repetition in tuple::',t1*2)

#printing iteration in tuple
print ('printing iteration in tuple')
for i in tuple:
    print (i)
#printing membership in tuple
print ('printing membership in tuple')
print ('is 1 in tuple ??::',1 in tuple)
print ('is 222 in tuple ??::',222 in tuple)
print ('is 3 in t1 ??::',3 in t1)
print ('is 5 in t2 ??::',5 in t2)
print ('is 15 in t2 ??::',15 in t2)
print ('is 15 not in t2 ??::',15 not in t2)
print ('is t1=t2 ??::',t1 is t2)
print ('is t1 is not t2 ??::',t1 is not t2)
