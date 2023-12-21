#1
def erzeuge3DFeld(n):
    return [[[i+j+k for k in range(n)] for j in range(n)] for i in range(n)]

    # Oder:
    # field = []
    # for i in range(n):
    #     field.append([])
    #     for j in range(n):
    #         field[i].append([])
    #         for k in range(n):
    #             field[i][j].append(i+j+k)
    # return field

#2
def summiertes3DFeld(n):
    field = erzeuge3DFeld(n)
    summed = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                summed += field[i][j][k]
    return summed

print(summiertes3DFeld(4))

#3
# Das Feld aufsummiert lässt sich beschreiben durch:
# sum (i = 0 bis n-1) [sum (j = 0 bis n-1) [sum (k = 0 bis n-1) [i+j+k]]]
# = sum (i = 0 bis n-1) [sum (j = 0 bis n-1) [n*i + n*j + sum (k = 0 bis n-1) [k]]]
# = sum (i = 0 bis n-1) [sum (j = 0 bis n-1) [n*i + n*j + (n-1)*n/2]]
# = sum (i = 0 bis n-1) [n*n*i + n*(n-1)*n/2 + n*sum (j = 0 bis n-1) [j]]
# = sum (i = 0 bis n-1) [n*n*i + n*(n-1)*n/2 + n*sum (j = 0 bis n-1) [j]]
# = n*n*(n-1)*n/2 + n*n*(n-1)*n/2 + n*n*sum (i = 0 bis n-1) [i]
# = n*n*(n-1)*n/2 + n*n*(n-1)*n/2 + n*n*(n-1)*n/2
# = 3*n*n*(n-1)*n/2
# = 3/2 * n^3*(n-1)