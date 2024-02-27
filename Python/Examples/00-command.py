import sys
def add(a,b):
    add = a + b
    return add
a = float(sys.argv[1])
operation = sys.argv[2]
b = float(sys.argv[3])

if operation == "add":
    output = add(a,b)
    print(output)