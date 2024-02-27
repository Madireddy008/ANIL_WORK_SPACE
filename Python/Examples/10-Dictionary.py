#DICTIONARY
d={1:'Anil',2:'Sravani','Moviya':1,'Kumar':2,}
print("Printing type of Dictionary d =",d,":",type(d))

#INDEXING IN DICTIONARY
print("Printing Indexing of 2 in d =",d,":",d[2])
print("Printing Indexing of 1 in d =",d,":",d[1])
print("Printing Indexing of 'Moviya' in d =",d,":",d['Moviya'])

#GET METHOD
print("Getting Key Value of 2 from Dictionary d =",d,":",d.get(2))

#KEYS METHOD
print("Getting Keys from Dictionary d =",d,":",d.keys())

#VALUES METHOD
print("Getting Values from Dictionary d =",d,":",d.values())

#ITEMS METHOD
print("Getting Items from Dictionary d =",d,":",d.items())

#UPDATE METHOD
d.update({11:222})
print("Updating Items in Dictionary d:",d)

#LOOPING IN Dictionary
for i in d:
    print(i)
    
for i in d.values():
    print(i)
    
for i,j in d.items():
    print(i,j)