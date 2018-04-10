def isPrime(i):
    for j in range(2,i):
        if (i%j==0):
            return False
    return True


num=600851475143
largest=0;
for i in range(int("%.0f" % num**(1/2))):
    if(num%i==0):
        if(isPrime(i)):
            largest=i
print(largest)