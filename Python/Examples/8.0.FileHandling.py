'''
Filehandiling:
   reading, writing, creating, deleting of a file is called filehandling
    Modes:
        r   -read
        w   -write (truncate)
        a   -append
        r+  -read write
        w+  -write read (truncate)
'''
print('WRITING DATA USING MODE W:')
f=open('8.1.Filehandling-demo.py',mode='w')
f.write("#This is for Testing Python FileHandling Writing")
f.close()

print('PRINTING WRITTEN DATA USING MODE W:')
f=open('8.1.Filehandling-demo.py',mode='r')
print(f.read())
f.close()

print('APPENDING DATA USING MODE A:')
f=open('8.1.Filehandling-demo.py',mode='a')
f.write("\n#This is for Testing Python FileHandling appending")
f.close()

print('PRINTING APPENDED DATA USING MODE A')
f=open('8.1.Filehandling-demo.py',mode='r')
print(f.read())
f.close()

print('APPENDING DATA USINF MODE R+:')
f=open('8.1.Filehandling-demo.py',mode='r+')
print(f.read())
f.write("\n#This is for Testing Python FileHandling Mode r+")
f.close()

print('PRINTING APPENDED DATA USING MODE R+')
f=open('8.1.Filehandling-demo.py',mode='r')
print(f.read())
f.close()

# print('WRITING MODE W+')
# f=open('8.1.Filehandling-demo.py',mode='w+')
# f.write("#This is for Testing Python FileHandling using Mode w+")
# print(f.read())
# f.close()

# print('PRINTING MODE W+')
# f=open('8.1.Filehandling-demo.py',mode='r')
# print(f.read())
# f.close()


# print('WRITING DATA USING MODE W LAST:')
# f=open('8.1.Filehandling-demo.py',mode='w')
# f.write("#This is for Testing Python FileHandling Writing LAST")
# f.close()

# print('PRINTING WRITTEN DATA USING MODE W LAST:')
# f=open('8.1.Filehandling-demo.py',mode='r')
# print(f.read())
# f.close()
