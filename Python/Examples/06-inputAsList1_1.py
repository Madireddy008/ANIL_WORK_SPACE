list = []
n = int(input("Enter elements"))
if n > 1:
    print("please enter", n, "integer Elements:")
    for i in range(0, n):
        ele = int(input())
        list.append(ele)
    print("please enter", n , "string values:")
    for i in range(0, n):
        ele = str(input())
        list.append(ele)
    print(list)     
else:
    print("please enter value graterthan 1")
