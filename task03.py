n = int(input("N: "))

if n <= 15:
    for i in range(n, 16):
        print(i, end=" ")
else:
    for i in range(n, 14, -1):
        print(i, end=" ")
