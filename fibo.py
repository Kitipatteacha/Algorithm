def fibo(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return fibo(num-2) + fibo(num-1)
num = int(input())
print("The " + str(num) + "th fibonacci number is: " + str(fibo(num)))
    
