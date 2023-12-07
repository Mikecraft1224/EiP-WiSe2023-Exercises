def loadMaps(file):
    # maps[etage][y][x]

    with open(file, "r") as f:
        lines = f.readlines()
        size = list(map(int, lines[0].split()))

        maps = []
        
        map1 = lines[1:size[0]+1]
        map2 = lines[size[0]+2:]
        maps.append([])
        maps.append([])

        for l in map1:
            maps[0].append(list(l.strip()))

        for l in map2:
            maps[1].append(list(l.strip()))

        return maps
    
def findChar(maps, char):
    for e in range(len(maps)):
        for y in range(len(maps[e])):
            for x in range(len(maps[e][y])):
                if maps[e][y][x] == char:
                    return (e, y, x)

def findPath(maps, posA, posB):
    # Erstelle 6 Etagen, 4 imaginäre für Etagenwechsel
    pre = {e:[[None for x in range(len(maps[0][0]))] for y in range(len(maps[0]))] for e in range(-2, 4)}

    # Etagenwechsel (0, 1, 1) zu (1, 1, 1)
    # (0, 1, 1), (2, 1, 1), (3, 1, 1) zu (1, 1, 1)
    # (1, 1, 1), (-1, 1, 1), (-2, 1, 1) zu (0, 1, 1)

    # Aufgebaut im Format
    #  ---->  2 ---->  3 ----|
    #  |                     v
    #  0                     1
    #  ^                     |
    #  |---- -2 <---- -1 <----
    # Ein Wechsel von 0 nach 1 MUSS durch die gerichteten Ebenen 2 und 3 gehen
    # Umgekert durch die Ebenen -1 und -2

    queue = [posA]

    while queue:
        pos = queue.pop(0)
        e, y, x = pos

        if pos == posB:
            return pre
        
        # Imaginäre Zwischenetagen
        if e == -1:
            queue.append((-2, y, x))
            pre[-2][y][x] = (e, y, x)
            continue
        elif e == -2:
            queue.append((0, y, x))
            pre[0][y][x] = (e, y, x)
            continue
        elif e == 2:
            queue.append((3, y, x))
            pre[3][y][x] = (e, y, x)
            continue
        elif e == 3:
            queue.append((1, y, x))
            pre[1][y][x] = (e, y, x)
            continue

        # Richtungen checken
        if maps[e][y][x + 1] != "#" and pre[e][y][x + 1] == None:
            queue.append((e, y, x + 1))
            pre[e][y][x + 1] = (e, y, x)
        if maps[e][y][x - 1] != "#" and pre[e][y][x - 1] == None:
            queue.append((e, y, x - 1))
            pre[e][y][x - 1] = (e, y, x)
        if maps[e][y + 1][x] != "#" and pre[e][y + 1][x] == None:
            queue.append((e, y + 1, x))
            pre[e][y + 1][x] = (e, y, x)
        if maps[e][y - 1][x] != "#" and pre[e][y - 1][x] == None:
            queue.append((e, y - 1, x))
            pre[e][y - 1][x] = (e, y, x)
        
        # Etagenwechsel
        if e == 0:
            # Überprüft ob ein Etagenwechsel möglich ist
            if maps[1][y][x] != "#" and pre[1][y][x] == None:
                queue.append((2, y, x))
                pre[2][y][x] = (e, y, x)
        elif e == 1:
            # Überprüft ob ein Etagenwechsel möglich ist
            if maps[0][y][x] != "#" and pre[0][y][x] == None:
                queue.append((-1, y, x))
                pre[-1][y][x] = (e, y, x)
    
    return pre

def getLength(pre, posA, posB):
    e, y, x = posB
    length = 0

    while posB != posA:
        posB = pre[e][y][x]

        e, y, x = posB
        length += 1

    return length

def printPath(maps, pre, posA, posB):
    e, y, x = posB

    while posB != posA:
        posB = pre[e][y][x]

        # Gibt nur Ebenen 0 und 1 aus
        if posB[0] in [0, 1]:
            # Überprüft in welche Richtung der Vorgänger von der aktuellen Position aus ist
            if posB[0] != e:
                maps[posB[0]][posB[1]][posB[2]] = "!"
            elif posB[1] > y:
                maps[posB[0]][posB[1]][posB[2]] = "^"
            elif posB[1] < y:
                maps[posB[0]][posB[1]][posB[2]] = "v"
            elif posB[2] > x:
                maps[posB[0]][posB[1]][posB[2]] = "<"
            elif posB[2] < x:
                maps[posB[0]][posB[1]][posB[2]] = ">"

        e, y, x = posB
    
    # print maps[0] and maps[1]
    print("\n".join(["".join(maps[0][y]) for y in range(len(maps[0]))]))
    print()
    print("\n".join(["".join(maps[1][y]) for y in range(len(maps[1]))]))



if __name__ == '__main__':
    maps = loadMaps("Blatt 06/zauberschule0.txt")
    posA = findChar(maps, "A")
    posB = findChar(maps, "B")
    pre = findPath(maps, posA, posB)
    print(getLength(pre, posA, posB))
    printPath(maps, pre, posA, posB)