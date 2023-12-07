# import copy
# copy.deepcopy(...)

def copy(X):
    Y = []
    for x in X:
        Y.append(x)
    return(Y)

def deepcopy(X):
    Y = []
    for x in X:
        if type(x) == list:
            Y.append(deepcopy(x))
        else:
            Y.append(x)
    return(Y)


a = [1,2,3,4]
b = a
c = deepcopy(a)

a[3] = 42

print(a,b,c)

A = [[1,2],[3,4]]
B = A
C = deepcopy(A)

A[1][1] = 42

print(A,B,C)
