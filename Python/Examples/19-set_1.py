'''
Set:
    -{} ex: s={1,2.2,3,"Anil"}
    -donot allow duplicates
    -no indexing, unordered
    -no slicing
    -donot allow mutable types as set elements
    SetMethods:
        add()
        update() -->bulk data adding
        pop()
        remove()
    SetOperations:
        union()   
        intersection()
        difference()
        issubset()
        issuperset()
'''
set1={1,2,3,4,5,6,7}
set2={1,3,5,7}
set3={1,2,3,4,5,6,7}
set4={1,3,5,7,9}
print('printing type of set1 & set2')
print(type(set1),type(set2))
print('Printing Using SetMethod add')
set1.add(234)
print(set1)
set1.add(10)
print(set1)
print('Printing Using SetMethod update')
set2.update({9,11,13,15})
print(set2)
print('Printing Using SetMethod pop')
set2.pop()
print(set2)
set2.pop()
print(set2)
print('Printing Using SetMethod remove')
set2.remove(5)
print(set2)
set2.remove(15)
print(set2)
print('Printing Using SetOperations union')
print(set3.union(set4))
print('Printing Using SetOperations intersection')
print(set3.intersection(set4))
print('Printing Using SetOperations difference')
print(set3.difference(set4))
print('Printing Using SetOperations difference')
print(set4.difference(set3))
print('Printing Using SetOperations issuperset')
print(set4.issuperset(set3))
print('Printing Using SetOperations issuperset')
print(set3.issuperset(set4))
print('Printing Using SetOperations issubset')
print(set4.issubset(set3))
print('Printing Using SetOperations issubset')
print(set3.issubset(set4))