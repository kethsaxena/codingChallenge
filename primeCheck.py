def isPrime(mynum):
    flag =True
    if mynum<=1:
        flag=False 
    elif mynum <=3:
        flag=True
    elif mynum % 2==0  or mynum % 3==0:
        flag=False
    
    #CORE LOOP
    i=5
    while i*i<=mynum:
        if mynum % i == 0 or mynum % (i+2) ==0:
            flag=False 
        i+=6
   
    return flag

def genPrime(lower:int,upper:int):
    return [x for x in range(lower,upper) if isPrime(x)]

# num=29

# if isPrime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.") 


print(genPrime(1,10))
