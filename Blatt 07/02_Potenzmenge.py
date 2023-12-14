import time

elements = 0

def potenzmenge(n,A):
    global elements

    if n == 0:
        elements += 1
        return([[]])
    P = []
    for M in potenzmenge(n-1,A):
        elements += 1
        P.append(M)
        P.append(M+[A[n-1]])
    return(P)

# print(potenzmenge(3,['a','b','c']))
# print(elements)

def teilmengen(n, k, A):
    if k == 0:
        return [[]]
    if k > n:
        return []
    if n == k:
        return [A]
    
    P = []
    # Liste der Teilmengen mit k-1 Elementen, da das letzte noch hinzugefügt werden muss
    for M in teilmengen(n - 1, k - 1, A):
        P.append(M)
        P.append(M + [A[n - 1]])
    # Liste der Teilmengen mit k Elementen, ohne das letzte Element
    for M in teilmengen(n - 1, k, A):
        P.append(M)
    # Somit beide Varianten abgedeckt

    return P


# def binomial(n, k):
#     if k == 0 or n == k:
#         return 1
    
#     return binomial(n - 1, k - 1) + binomial(n - 1, k)


def binomialMemo(n, k):
    memo = [[None for _ in range(k + 1)] for _ in range(n + 1)]

    def binomial(n, k):
        if k == 0 or n == k:
            memo[n][k] = 1
            return 1

        if memo[n][k] is None:
            memo[n][k] = binomial(n - 1, k - 1) + binomial(n - 1, k)
        
        return memo[n][k]
    
    return binomial(n, k)


start = time.perf_counter_ns()
print(binomialMemo(100, 50))
print(f"Time: {time.perf_counter_ns() - start}ns")