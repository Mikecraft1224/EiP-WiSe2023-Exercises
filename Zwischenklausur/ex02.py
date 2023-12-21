#1
def hatPeriode(a, k):
    for i in range(1, len(a)):
        if a[i] != a[i%k]:
            return False
    return True

#2
def kleinstePeriode(a):
    for k in range(1, len(a)):
        if hatPeriode(a, k):
            return k
    return len(a)

# Tests
a = [2,3,1,2,2,3,1,2,2,3,1,2,2,3]
print(hatPeriode(a, 3))
print(hatPeriode(a, 8))
print(kleinstePeriode(a))