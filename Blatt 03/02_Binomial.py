until = int(input("Until row: "))

for n in range(until+1):

    # prints the n-th row
    for k in range(n+1):
        i = 0
        b = 1

        while i < k:
            b = b * (n-i)
            b = b // (i+1)
            i = i + 1

        print(b, end=" ")
    print()