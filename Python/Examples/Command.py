#Commandline Arguments

#Importing sys for Commandline Arguments
import sys

#Functions Definition
def add(num1, num2):
    add = num1 + num2
    return add
def sub(num1, num2):
    sub = num1 - num2
    return sub
def mul(num1, num2):
    mul = num1 * num2
    return mul
def div(num1, num2):
    div = num1 / num2
    return div
def mod(num1, num2):
    mod = num1 % num2
    return mod

#we need to convert the arguments into float
num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == '+':
    output = add(num1, num2)
    print(output)
elif operation == '-':
    output = sub(num1, num2)
    print(output)
elif operation == '*':
    output = mul(num1, num2)
    print(output)
elif operation == '/':
    output = div(num1, num2)
    print(output)
elif operation == '%':
    output = mod(num1, num2)
    print(output)
else:
    print("Invalid input")