n = int(input("Enter the principle amount:"))

rate = int(input("Enter the rate:"))

years = int(input("Enter the number of years:"))

for i in range(years):
    n = n + ((n * rate) / 100)

print(n)