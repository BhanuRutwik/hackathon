def gcd(a,b):
    print('2asfasf')
    small=1
    gd=0
    if a>b:
        small==b
    else:
        small==a
    for i in range(1, small+1):
        if((a % i == 0) and (b % i == 0)):
            gd=i
    return gd
a = 5
b = 8
t=gcd(a,b)
print("GCD :",t)