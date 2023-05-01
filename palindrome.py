def palindrome():
    print('program for palindrome')
    #program to check given number is palindrome or not
    
    n = 121
    temp=n #storing the number in temporary variable
    rev=0
    while(n>0):
        digit=n/10
        rev=rev*10+digit #reversing the digit and storing it in a variable
        n=n//10
    if (temp==rev) : #comparing temp variable and rev variable
        print('palindrome')
        print("It is a palindrome number")
    else:
        print("It is not a palindrome")
palindrome()
print("palindrome program")