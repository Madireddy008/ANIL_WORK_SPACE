#SET IN PYTHON
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
set3={1,2,3}
set4={4,5,6}
print("Printing type of set1 =",set1,":",type(set1))

#ADD METHOD IN SET
set1.add(9)
print("Printing added set1:", set1)

#UPDATE METHOD IN SET
set4.update({11,12,13})
print("Printing Updated set4:", set4)

#POP METHOD IN SET
set1.pop()
print("Printing Popped set1:", set1)

#REMOVE METHOD IN SET
set1.remove(9)
print("Printing Removed set1:", set1)

#ADD METHOD IN SET
set1.add(1)
print("Printing added set1:", set1)

#REMOVE METHOD IN SET
set4.remove(11)
set4.remove(12)
set4.remove(13)
print("Printing Removed set4:", set4)

#UNION OPERATION IN SET
print("Union of set1 =",set1,"and set2 =",set2,":",set1.union(set2))

#Intersection OPERATION IN SET
print("Intersection of set1 =",set1,"and set2 =",set2,":",set1.intersection(set2))

#DIFFERENCE OPERATION IN SET
print("Difference of set1 =",set1,"and set2 =",set2,":",set1.difference(set2))
print("Difference of set2 =",set2,"and set1 =",set1,":",set2.difference(set1))

#ISSUBSET OPERATION IN SET
print("Is set1 =",set1,"is subset of set3 =",set3,"?:",set1.issubset(set3))
print("Is set3 =",set3,"is subset of set1 =",set1,"?:",set3.issubset(set1))

#ISSUPERSET OPERATION IN SET
print("Is set1 =",set1,"is superset of set3 =",set3,"?:",set1.issuperset(set3))
print("Is set3 =",set3,"is superset of set1 =",set1,"?:",set3.issuperset(set1))

#LOOPING IN SET
for i in set1:
    print(i)
