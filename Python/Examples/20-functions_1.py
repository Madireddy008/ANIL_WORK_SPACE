'''
Function:
    -is a block of a code
    -only runs when it is called
    Syntax:
        def function.name()
        Ex:
            def add(a,b)
                return a+b
            print(add(1,2))
'''
# def func():#function defination
#     print("this is function") #function body
# func() #function call

def func(a,b,c):#function defination
    print("Output-->",a,b,c) #function body
func(1,2,3) #function call

def func(*a):#function defination with arbitary arguments
    print("Output will be in a Tuple-->",a) #function body
func(1,2,3) #function call and out put will be in tuple format

def func(**a):#function defination with keyword arguments
    print("Output will be in a Dictionary-->",a) #function body
func(a=1,b=2) #function call and out put will be in dictionary format

print('Printing Nested functions defination')
def outer():
    print('Outer')
    def inner():
        print('Inner')
    inner()
outer()

print('Printing addition function')
def add(a,b):
    print(a+b)
    def multiply(c,d):
        print(c*d)
    multiply(1,2)
add(1,2)

def addition(a,b):
    print(a+b)
def subraction(a,b):
    print(a-b)
    