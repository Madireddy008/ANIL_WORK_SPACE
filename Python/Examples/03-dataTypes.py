'''
DataTypes in Python
1.Int
    a=1
2.Boolean
    0=false
    1=true
3.Float
    a=1.2
4.String
    a='ANIL KUMAR REDDY'
5.Complex
    a=1+2j
6.List
    []
7.Tuple
    ()
8.Set
    {}
9.Dictinoary
    {}
'''
# Integer Examples
print ('Integer Examples')
a=10
b=-10
print(type(a),type(b))

# Boolean Examples
print ('Boolean Examples')
c=True
d=False
print(type(c),type(d))
print(True==1)
print(False==0)
print(True==0)
print(False==1)

# Float Examples
print ('Float Examples')
e=4.44
print(type(e))

# Complex Examples
print ('Complex Examples')
f=1+2j
print(type(f))

# DataTypes Conversion
'''
int()
float()
bool()
str()
'''
print ('DataTypes Conversion')
g=2
h=2.5
i=20
#No Data Loss --> Implicit Type Conversion
print ('No Data Loss --> Implicit Type Conversion')
print (float(g))
#Data Loss --> Explicit Type Conversion
print ('Data Loss --> Explicit Type Conversion')
print (int(h))