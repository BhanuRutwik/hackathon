def insort(a):
    print("file is changed")
    print('insertion sort')
    for i in range(1, len(a)):
        b = a[i]
        j = i - 1
        while j >= 0 and b < a[j]:
            a[j], a[j + 1] = a[j + 1], a[j]
            j -= 1

a = [5, 6, 4, 1, 3, 2]
insort(a)
for i in a:
    print(i)