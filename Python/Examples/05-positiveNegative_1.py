import sys
#num = int(sys.argv[1])
num = int(input("enter any number"))
if num > 0:
    print(num, "is positive number")
elif num < 0:
    print(num, "is negative number") 
else:
    print(num, "is whole number")
