'''
which will store a value 
or 
address of a value

syntax:
    variableName = value
    where value is string, integer,boolean,float etc.. any data type

rules of variables:
notstart with digit or symbol
start with alphabet or _
case sensitive
'''
a = 10
b = 'ten'
c = 10.10
# below is not allowed one value cannot be given to multiple variables
#a,b,c = 10
d, e, f = 1,2,3 #this is allowed
g = h = i = 20
print("printimg the values of all variables: \n", "\n",a, "\n",b,"\n",c ,"\n",d, "\n",e, "\n",f, "\n",g, "\n",h, "\n",i)
print(id(a))
