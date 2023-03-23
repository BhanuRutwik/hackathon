#Program to print Fibonacci series
n= int(input("enter the number of elements you want in series:"))
c=[]
c.append(0)
c.append(1)
a=0
b=1
d=0
for i in range( 1, n-1):
    d=a+b
    c.append(d)
    a=b
    b=d
for i in c:
    print(i)