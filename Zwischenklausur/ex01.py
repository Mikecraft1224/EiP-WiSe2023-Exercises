#i
def f(n):
    i = 0
    while n > 1:
        n /= 2 # n = n / 2
        i += 1
    return i

#ii
def r(n):
    if n <= 1:
        return 0
    return r(n/2) + 1

#iii
import math

def c(n):
    return math.ceil(math.log(n, 2)) # Aufgerundet