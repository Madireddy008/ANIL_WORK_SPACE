a = range(0, 25)
for i in a:
    if i >= 18:
        print("For i=",i, ":you can vote now")
    # if we remove else block only satisfied condition of if block will come 
    else:
        print("For i=",i,":you cannot vote now wait till 18")
    