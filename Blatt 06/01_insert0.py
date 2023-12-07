import time

for k in range(1, 7):
    n = 10**k

    startTime = time.perf_counter()
    A = []
    for i in range(n):
        A.append(i)
    print(f"A: {time.perf_counter() - startTime}")

    startTime = time.perf_counter()
    B = []
    for i in range(n-1,-1,-1):
        B.insert(0,i)
    print(f"B: {time.perf_counter() - startTime}")