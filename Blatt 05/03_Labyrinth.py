import time, os

def readField(path):
    with open(path, "r", encoding="utf-8") as f:
        return [list(line.strip()) for line in f.readlines()]
    
def printField(field):
    print("\n".join(["".join(row) for row in field]))

def searchChar(field, char):
    for z in range(len(field)):
        for s in range(len(field[z])):
            if field[z][s] == char:
                return (z, s)
    
    return None

def searchPath(field, start, end):
    prev = [[None for s in range(len(field[z]))] for z in range(len(field))]
    queue = [start]
    copyField = [row[:] for row in field]

    while len(queue) > 0:
        time.sleep(1/50)
        os.system("cls")

        printField(copyField)

        z, s = queue.pop(0)

        for dz in range(-1, 2):
            for ds in range(-1, 2):
                if dz != 0 and ds != 0:
                    continue

                if 0 <= z + dz < len(field) and 0 <= s + ds < len(field[z]):
                    if field[z + dz][s + ds] != "█" and prev[z + dz][s + ds] == None:
                        copyField[z + dz][s + ds] = "x"
                        prev[z + dz][s + ds] = (z, s)
                        queue.append((z + dz, s + ds))
                
                # if (z + dz, s + ds) == end:
                #     return prev
            
    return prev

def printPath(field, prev, start, end):
    z, s = end
    z, s = prev[z][s]

    while (z, s) != start:
        field[z][s] = "x"
        z, s = prev[z][s]
    
    printField(field)

if __name__ == '__main__':
    field = readField("Blatt 05/labyrinth.txt")
    printField(field)

    start = searchChar(field, "S")
    end = searchChar(field, "Z")

    prev = searchPath(field, start, end)
    printPath(field, prev, start, end)