# 1. Da die Blöcke jeweils in den einzelnen Zellen von C stehen, lässt sich damit rechnen.
#   Wenn wir nun Blöcke abziehen und den Schnitt der Blöcke wieder addieren, erhalten wir die Summe der Elemente in dem Rechteck.

# 2. Es werden maximal (n x m) x (n x m) = n^2 x m^2 Addition benötigt. (Obere Grenze)

# 3. Die Matrix B berechnet die Summen der Zeilen von A.
#   Die Matrix C berechnet die Summen der Spalten von B.
#   Somit müssen Zeilensummen nicht mehrfach berechnet werden.

# 4. 
with open("Blatt 05/A.txt", "r") as f:
    A = [[int(x) for x in line.strip().split()] for line in f.readlines()]

B = A

for s in range(1, len(A[0])):
    for z in range(len(A)):
        B[z][s] += B[z][s - 1]

C = B

for z in range(1, len(A)):
    for s in range(len(A[0])):
        C[z][s] += C[z - 1][s]

with open("Blatt 05/C.txt", "w") as g:
    g.write("\n".join([" ".join([str(x) for x in C[z]]) for z in range(len(C))]))

# 5.
def findSum(C, sum):
    # Naive Implementierung, binäre Suche möglich
    for s1 in range(len(C[0])):
        for s2 in range(s1, len(C[0])):
            for z1 in range(len(C)):
                for z2 in range(z1, len(C)):
                    if C[z2][s2] - C[z2][s1 - 1] - C[z1 - 1][s2] + C[z1 - 1][s1 - 1] == sum:
                        return (z1, s1, z2, s2)
    
    return None

print(findSum(C, 314159265))