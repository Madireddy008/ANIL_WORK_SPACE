def prime(number):
    for num in range(2,number):
        status = True
        for i in range(2,num):
            if num % i == 0:
                status = False
        if status:
            print(num)
prime(101)