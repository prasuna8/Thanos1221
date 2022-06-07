sal=int(input("enter salary"))
hra=int(input("enter hra"))
ded=int(input("enter deductions"))
net_sal=sal-(hra+ded)
if(sal<300000):
        tax=0
elif(sal>=300000 and sal<600000):
    tax=(10/100)*net_sal
elif(sal>=600000 and sal<1000000):
    tax=(15/100)*net_sal
else:
    tax=(20/100)*net_sal
print("tax =",tax)
