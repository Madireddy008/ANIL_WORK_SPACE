n = int(input("enter a number:"))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print(i, "primeNumber")
else:
    print(i, "notPrimeNumber")

'''
n = int(input("enter a number:"))
for i in range(1, n):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count+= 1
    if count == 2:
        print(i, "is a prime Number")
    else:
        print(i, "is nota prime Number")
'''