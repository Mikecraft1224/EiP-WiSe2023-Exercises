#1
def zeilensumme(M, i):
    summed = 0
    for e in M[i]:
        summed += e
    return summed

    # Oder:
    # return sum(M[i])

#2
def spaltensumme(M, j):
    summed = 0
    for e in M:
        summed += e[j]
    return summed

    # Oder:
    # return sum([e[j] for e in M])

#3
def istMagisch(M):
    # Diagonale
    diag = 0
    for i in range(len(M)):
        diag += M[i][i]
    
    # Gegen-Diagonale
    revDiag = 0
    for i in range(len(M)):
        revDiag += M[i][-i - 1]

    if diag != revDiag:
        return False
    
    # Zeilen und Spalten
    for i in range(len(M)):
        if zeilensumme(M, i) != diag:
            return False
        
        if spaltensumme(M, i) != diag:
            return False
        
    return True

#4
def magischesQuadrat(n):
    M = [[0 for i in range(n)] for j in range(n)]
    möglichkeiten = [i for i in range(1, n**2+1)]
    
    def magischesQuadratHelfer(M, x, y):
        if x == n and y == 0:
            return istMagisch(M)
        
        if x == n:
            return magischesQuadratHelfer(M, 0, y-1)
        
        for k in range(len(möglichkeiten)):
            M[x][y] = möglichkeiten[k]
            möglichkeiten.pop(k)
            if magischesQuadratHelfer(M, x+1, y):
                return True
            möglichkeiten.insert(k, M[x][y])

        return False
    
    if magischesQuadratHelfer(M, 0, n-1):
        return M

#5
# Die Summe aller Zahlen im Quadrat lässt sich beschreiben durch
#       n^2 * (n^2 + 1) / 2
# Da aber die Zeilen- und Spaltensummen gleich sind, muss jede Zeile und Spalte
# den Durchschnittswert haben, also
#       n^2 * (n^2 + 1) / 2 / n = n * (n^2 + 1) / 2


