'''
Dictionary:
    -{}
    -key:value data
            d={'a':123,1:"abc"}
            a=key
            123=value
            key:value == item
    -key should be immutable
    -value should be mutable (different type)
    -key will act as index (but normal indexing will not work)
    -no slicing
    -keys are unique
    Methods:
        -get()      -->fetching the elements using input as key
        -update()   -->updating the values in dictionary
        -values()   -->values in dictionary
        -keys()     -->Keys in dictionary
        -items()    -->items in dictionary
'''
d={1:'abc',2:'Anil','kumar':3,4:'madireddy'}
# printing d variable type
print('printing d variable type')
print(type(d))
print('printing Dictionary Values using Dictionary Keys')
print(d[1])
print(d[2])
print(d['kumar'])
print(d[4])
#printing dictionary methods uding methods
print('printing dictionary methods uding methods in d')
print(d.get(1))
print(d.get(2))
print(d.get('kumar'))
print(d.get(4))
print('printing keys in dictionary d')
print(d.keys())
print('printing values in dictionary d')
print(d.values())
print('printing items in dictionary d')
print(d.items())
print('updating items in dictionary d')
d.update({17:'Kanya'})
print(d)
print('printing keys in dictionary d using for')
for i in d.keys():
    print(i)
print('printing values in dictionary d using for')
for i in d.values():
    print(i)
print('printing items in dictionary d using for')
for i in d.items():
    print(i)
print('printing values in dictionary d using for')
for i,j in d.items():
    print(i,j)