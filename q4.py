def checkprime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c+=1
            break
        else:
            continue
    if(c==1):
        print("not a prime number")
    else:
        print("prime number")

def dbyfive(n):
    if(n%5==0):
        print("divisible by 5")
    else:
        print("not divisible by 5")

def evenorodd(n):
    if(n%2==0):
        print("even number")
    else:
        print("odd number")

def sum1(n):
    sumofn=(n*(n+1))/2
    print("sum of n is ",sumofn)

n=int(input("enter a number"))
checkprime(n)
dbyfive(n)
evenorodd(n)
sum1(n)
