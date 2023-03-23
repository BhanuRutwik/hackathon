n= int(input("Enter the number you want to find the factorial of: "))
prod=1
for i in range(1,n+1):
    prod=prod*i
print(prod)