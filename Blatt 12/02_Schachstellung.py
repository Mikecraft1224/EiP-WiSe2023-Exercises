class Schachstellung:
    def __init__(self):
        self.brett = [['.' for j in range(8)] for i in range(8) ]

    # 2.2
    def __hash__(self):
        return hash("\n".join([" ".join(line) for line in self.brett]))
    
    def __eq__(self,other):
        return hash(self) == hash(other)
        # return self.brett == other.brett

# 2.3
C = []
K = []

with open("Blatt 12/Carlsen.txt", "r") as f:
    j = 0
    board = Schachstellung()

    for row in f.readlines():
        row = row.strip()
        if row == "":
            # if board not in C:
            C.append(board)
            board = Schachstellung()
            j = 0
            continue

        for i, col in enumerate(row):
            board.brett[j][i] = col
        j += 1

with open("Blatt 12/Keymer.txt", "r") as f:
    for row in f.readlines():
        board = Schachstellung()
        i, j = 0, 0

        for char in row.strip().split()[0]:
            if char == "/":
                j += 1
                i = 0
            elif char.isdigit():
                i += int(char)
            else:
                board.brett[j][i] = char
                i += 1
        
        # if board not in K:
        K.append(board)

C = set(C)
K = set(K)

CK = C.intersection(K)

# for board1 in C:
#     for board2 in K:
#         if board1 == board2:
#             CK.add(board1)

print(len(CK))
