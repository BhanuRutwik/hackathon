def dectobin(n):
    if n>1:
        dectobin(n/2)
    print(n%2,end='')
    print('decimal to binary program')
n=24
dectobin(n)
print("dec to bin")