a={1:'abc', 22:'kiran', 'pythonlife':1}
print(type(a))
print(a.get(22))
print(a.keys())
print(a.values())
print(a.items())
a.update({3:'sravani'})
print(a)

for i in {1:'abc', 22:'kiran', 'pythonlife':1}.keys():
    print(i)
for i in {1:'abc', 22:'kiran', 'pythonlife':1}.values():
    print(i)
for i in {1:'abc', 22:'kiran', 'pythonlife':1}.items():
    print(i)