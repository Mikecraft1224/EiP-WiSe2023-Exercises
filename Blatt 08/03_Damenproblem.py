#1 
# Da das Gitter 2^n * 2^n groß ist, gibt es (2^n)^2 Felder.
# Initial ist ein Feld besetzt, also gibt es (2^n)^2 - 1 Felder die noch besetzt werden müssen.
# Jede Kachel deckt hierbei 3 Felder ab, weshalb (2^n)^2 - 1 durch 3 teilbar sein muss.

#2
# Durch die Divide and Conquer Strategie wird das Problem in kleinere Teilprobleme zerlegt.
# Hierbei beginnt das Problem mit einem 2^n * 2^n großen Gitter, welches in 4 2^(n-1) * 2^(n-1) große Gitter zerlegt wird.
# Das Startgitter hat dabei ein besetztes Feld.
# Wenn man nun eine Kachel so auf das Startgitter legt, dass in jedem der 4 Teilgitter ein Feld besetzt ist, so hat man nun 4 Teilprobleme.
# Diese können nun wieder auf die gleiche Art und Weise gelöst werden.
# Dies wird solange wiederholt, bis das Gitter nur noch aus vier Feldern besteht, da hierbei mit einer Kachel alle Felder abgedeckt werden können.

#3
count = 0

def zulaessig(S):
    k = len(S)
    for i in range(k-1):
        if S[i] == S[k-1]:
            return(False)
        if abs(S[k-1]-S[i]) == k-1-i:
            return(False)
    return(True)

def vervollstaendige(S):
    global count

    if len(S) == n:
        count += 1
        return
    for i in range(n):
        S.append(i)
        if zulaessig(S):
            vervollstaendige(S)
        S.pop()

n = 10
S = []
vervollstaendige(S)
print(S)
print(n, count)