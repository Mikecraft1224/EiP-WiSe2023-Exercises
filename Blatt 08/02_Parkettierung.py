k = 3
board = [[-1 for i in range(2**k)] for j in range(2**k)]
board[2][6] = 0
currentNumber = 1

# x=0 und y=0 setzen Standardwerte falls diese nicht angegeben werden
def parkettiere(l, x=0, y=0):
    global board, currentNumber
    
    # Abbruchbedingung
    if l == 2:
        for i in range(2):
            for j in range(2):
                if board[y+j][x+i] == -1:
                    board[y+j][x+i] = currentNumber
        currentNumber += 1
        return
    
    # Quadrant bestimmen
    quadrant = None
    for i in range(l):
        for j in range(l):
            if board[y+j][x+i] != -1:
                if i < l/2 and j < l/2:
                    quadrant = 1
                elif i >= l/2 and j < l/2:
                    quadrant = 2
                elif i < l/2 and j >= l/2:
                    quadrant = 3
                elif i >= l/2 and j >= l/2:
                    quadrant = 4
                break
        if quadrant != None:
            break

    # Parkettierung
    if quadrant != 1:
        board[y + l//2 - 1][x + l//2 - 1] = currentNumber
    if quadrant != 2:
        board[y + l//2 - 1][x + l//2] = currentNumber
    if quadrant != 3:
        board[y + l//2][x + l//2 - 1] = currentNumber
    if quadrant != 4:
        board[y + l//2][x + l//2] = currentNumber
    currentNumber += 1

    # Rekursion 
    parkettiere(l//2, x, y)
    parkettiere(l//2, x+l//2, y)
    parkettiere(l//2, x, y+l//2)
    parkettiere(l//2, x+l//2, y+l//2)


parkettiere(2**k)
# f"{i:>2}" formatiert die Zahl i so, dass sie mindestens 2 Zeichen lang ist und rechtsbündig ist
# z.B. 1 wird zu " 1", 10 wird zu "10"
print("\n".join([" ".join([f"{i:>2}" for i in row]) for row in board]))