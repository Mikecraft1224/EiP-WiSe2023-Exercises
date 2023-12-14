# Das eindimensionale Feld der Staedtenamen.
stadt = ['MZ', 'KO', 'TR', 'SP', 'WO', 'KL', 'LU']

# Das zweidimensionale Feld der Abstandstabelle.
dist = [[0, 61, 119, 77, 41, 71, 61],
        [61, 0, 95, 129, 97, 101, 116],
        [119, 95, 0, 137, 124, 87, 133],
        [77,129, 137, 0, 35, 50, 17],
        [41, 97, 124, 35, 0, 48, 19],
        [71, 101, 87, 50, 48, 0, 49],
        [61, 116, 133, 17, 19, 49, 0]]

def allePermutationen(n,A,P):
    def swap(A,i,j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

    if n == 0:
        P.append([A[i] for i in range(len(A))])
    for i in range(n-1,-1,-1):
        swap(A,i,n-1)
        allePermutationen(n-1,A,P)
        swap(A,i,n-1)

# P = []
# allePermutationen(3,[1,2,3],P)
# print(P)

def distanz(P):
    d = 0

    # for i in range(len(P)-2):
    #     d += dist[P[i]][P[i+1]]
    # d += dist[P[-1]][P[0]]

    for i in range(len(P) - 1, -1, -1):
        d += dist[stadt.index(P[i])][stadt.index(P[i - 1])]

    return d

perms = []
allePermutationen(len(stadt), stadt, perms)
shortedPath = None
shortestPathLength = float('inf')

for perm in perms:
    d = distanz(perm)
    if d < shortestPathLength:
        shortestPathLength = d
        shortedPath = perm

print(shortedPath)
print(shortestPathLength)