import random

random.seed(4242)

n = 22
Gewicht = [random.randint(20,100) for i in range(n)]
Wert = [random.randint(20,100) for i in range(n)]

Gmax = 500

def potenzmenge(n,A):
    if n == 0:
        return([[]])
    P = []
    for M in potenzmenge(n-1,A):
        P.append(M)
        P.append(M+[A[n-1]])
    return(P)

GewichtP = potenzmenge(n,Gewicht)
WertP = potenzmenge(n,Wert)

best = None
bestWert = 0

for i in range(len(GewichtP)):
    if sum(GewichtP[i]) <= Gmax and sum(WertP[i]) > bestWert:
        best = GewichtP[i]
        bestWert = sum(WertP[i])

# for g, w in zip(GewichtP, WertP):
#     if sum(g) <= Gmax and sum(w) > bestWert:
#         best = g
#         bestWert = sum(w)


print('Gewichte:',Gewicht)
print('Werte:',Wert)
print('Gmax:', Gmax)
print('Beste Loesung:', best)
print('Gewicht:', sum(best))
print('Wert:', bestWert)
