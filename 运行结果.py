import numpy as np


def fun(n):
    sartm = int(np.sqrt(n))
    i=2
    while i<=sartm:

        if(n%i== 0):
            return False
        i+=1
    return True



a=10
b=30
I=0

if (a%2== 0):
    a+=1
m=a
while m<b:
    if fun(m):
        if I%10==0:
            I+=1
            print("")
    print(m)
    m+=2
