import time, IPython.display
import os, sys
from copy import deepcopy

m = 26 # Zahl der Zeilen
n = 100 # Zahl der Spalten

G = [ ['.' for s in range(n)] for z in range(m)]

# Gleiter
G[0][1] = 'o'
G[1][2] = 'o'
G[2][0] = 'o'
G[2][1] = 'o'
G[2][2] = 'o'

# f-Pentomino
G[m//2-1][n//2] = 'o'
G[m//2-1][n//2+1] = 'o'
G[m//2][n//2-1] = 'o' 
G[m//2][n//2] = 'o' 
G[m//2+1][n//2] = 'o'

for i in range(100):
    time.sleep(0.1)
    os.system("cls")

    # Berechne die neue Generation
    H = [ ['.' for s in range(n)] for z in range(m)]

    for z in range(m):
        for s in range(n):
            c = 0

            for dz in range(-1, 2):
                for ds in range(-1, 2):
                    if dz == 0 and ds == 0:
                        continue
                    
                    # mit Rand
                    if 0 <= z + dz < m and 0 <= s + ds < n:
                        if G[z + dz][s + ds] == 'o':
                            c += 1

                    # # ohne Rand
                    # zi = z + dz if z + dz < m else 0
                    # si = s + ds if s + ds < n else 0
                    # if G[zi][si] == 'o':
                    #     c += 1
            
            if G[z][s] == 'o':
                if c == 2 or c == 3:
                    H[z][s] = 'o'
            else:
                if c == 3:
                    H[z][s] = 'o'
    
    G = [[H[z][s] for s in range(n)] for z in range(m)]

    print("\n".join(["".join(G[z]) for z in range(m)]))
    