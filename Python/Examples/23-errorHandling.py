'''
Error Handling in Python:
    -interrupting normal execution of coe is called error or exception
    -These interruptions are handled by using the error handling
    -error handling is done by below blocks
    1. try:
        risky code.
            -the code which we expect error in future are written under try.        
    2. except:
        print("error")
            -Incase of error in try except will execute.
    3. else:
        print("no error")
            -Incase if you have no errors in try then else will execute.
    4. finally:
        print("always")
            -Incase if in all 3 fields errors may or maynot be but finally will execute always. 
'''
a = 1
try:
    print(anil)#if you replace a with anil then error handle comes
    print("Anil")
except:
    print("error")
else:
    print("no error")
finally:
    print("always")


#
try:
    print("Anil")
except:
    print("error")
else:
    print("no error")
finally:
    print("always")


#
try:
    print("Anil" + 33)
except TypeError:
    print("typeError")
except ValueError:
    print("valueError")
else:
    print("no error")
finally:
    print("always")