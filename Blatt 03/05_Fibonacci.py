# 1
def fib(n):
    # fibs = [0, 1]

    # for i in range(2, n+1):
    #     fibs.append(fibs[i-1] + fibs[i-2])

    # return fibs[n]
    
    a = 0
    b = 1

    for i in range(2, n+1):
        print(a, end=" ")

        c = a + b
        a = b
        b = c

    print(f"{a} {b}")


# 2
def form(n):
    return round((1/5**0.5) * (((1+5**0.5)/2)**n - ((1-5**0.5)/2)**n), 0)

def fibonacciFormula(n):
    a = 0
    b = 1

    print(f"0: {a} {form(0)}")
    print(f"1: {b} {form(1)}")

    for i in range(2, n+1):
        c = a + b
        a = b
        b = c

        print(f"{i}: {c} {form(i)}")


# 3
def fibList(n):
    fibs = [0, 1]

    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])

    return fibs

n = 99
fibs = fibList(n+1)

summed = 0
for i in range(0, n - 1):
    summed += fibs[i]

if summed == fibs[n] - 1:
    print("Summe stimmt")
else:
    print("Summe stimmt nicht")


# 4
def fibPrimes(n):
    fibs = [0, 1]

    # Calculate fibonacci numbers
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])

    # Calculate primes
    primes = []
    for i in range(0, n+1):
        if fibs[i] > 1:
            for j in range(2, int(fibs[i]**0.5 + 1)):
                if (fibs[i] % j) == 0:
                    break
            else:
                primes.append(fibs[i])
        
    return primes

print(fibPrimes(30))