#IF
age=15
if age>17:
    print("You can vote")
else:
    print("you cannot vote")
    

#ELIF
age1=18
if age1>18:
    print("You can vote1")
elif age1==18:
    print("you can vote1")
else:
    print("you cannot vote1")
    

#NESTED IF
door='open'
door1='close'
if door=='open':
    print("Watch Inside")
    if door1=='close':
        print("Open and Watch")
    else:
        print("Watch Normally")
else:
    print("open and watch")