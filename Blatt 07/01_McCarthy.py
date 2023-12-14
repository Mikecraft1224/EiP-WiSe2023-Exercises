# 1
def sum(n, A):
    if n == 0:
        return 0
    
    return sum(n - 1, A) + A[n - 1]


# 2
def ggT(a, b):
    # if b > a:
    #     # return ggT(b, a)
    #     a, b = b, a

    if b == 0:
        return a
    
    # für b > a => a % b = a
    return ggT(b, a % b)


# 3
def f(n):
    if n > 100:
        return(n-10)
    return(f(f(n+11)))

print(f(42))


# 4
def collatzRec(n):
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return collatzRec(n / 2)
    
    return collatzRec(3 * n + 1)

def collatzIter(n):
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    
    return 1

# for i in range(1, 10**6 + 1):
#     if collatzRec(i) != 1:
#         print(f"Fehler bei {i} (rekursiv)")
#         break
#     if collatzIter(i) != 1:
#         print(f"Fehler bei {i} (iterativ)")
#         break
# else:
#     print("Alle Ergebnisse sind 1")

# 5
def palindrom(word):
    if len(word) <= 1:
        return True
    
    return word[0] == word[-1] and palindrom(word[1:-1])

print(palindrom("aasddnna"))