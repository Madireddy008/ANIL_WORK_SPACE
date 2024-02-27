#Single Quote Declaration
a='Anil Kumar Reddy'

#Double Quote Declaration for ['s]
b="Anil Kumar Reddy's"

#Triple Quote Declaration for multiline Storing
c='''Anil Kumar Reddy'''

d="Anil Kumar Reddy"
e="  Madireddy Anil  "

print(type(a),type(b),type(c))
print("Upper of",d, ":",d.upper())
print("Lower of",d, ":",d.lower())
print("EndsWith of",d, ":",d.endswith('Reddy'))
print("StartsWith of",d, ":",d.startswith('Anil'))
print("Replace of",d, ":",d.replace('Reddy','Reddy Madireddy'))
print("Find of",d, ":",d.find('Kumar'))
print("Index of",d, ":",d.index('Reddy'))
print("Find of",d, ":",d.find('Sravani'))
# print("Index of Anil Kumar Reddy:",d.index('Sravani'))
print("Count of",d, ":",d.count('d'))
print("RemovePrefix of",d, ":",d.removeprefix('Anil'))
print("RemoveSuffix of",d, ":",d.removesuffix('Reddy'))
print("Split of",d, ":",d.split())
print("Length of",e, ":",len(e))
print("Strip of",e, ":",e.strip())
print("Rstrip of",e, ":",e.rstrip())
print("Lstrip of",e, ":",e.lstrip())
x=e.strip()
print(x)
print("Length of",x, ":",len(x))
print("Length of Madireddy:",len('Madireddy'))