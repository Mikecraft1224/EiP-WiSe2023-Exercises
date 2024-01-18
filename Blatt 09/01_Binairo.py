B1 = [[0, 0, 0, 2, 0, 0],
      [1, 0, 1, 0, 0, 0],
      [0, 2, 0, 2, 0, 2],
      [0, 0, 0, 0, 0, 0],
      [1, 0, 0, 2, 0, 0],
      [0, 0, 1, 0, 0, 0]]

B2 = [[0, 1, 2, 0, 0, 2, 1, 1, 0, 1],
      [0, 2, 1, 2, 0, 0, 1, 0, 1, 1],
      [1, 2, 0, 0, 0, 0, 2, 1, 0, 2],
      [0, 1, 2, 0, 0, 1, 0, 0, 2, 0],
      [2, 0, 0, 0, 2, 0, 1, 2, 1, 0],
      [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
      [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0, 2, 1],
      [1, 0, 2, 1, 0, 2, 2, 0, 2, 0]]

B3 = [[2, 1, 0, 0, 1, 0, 1, 1, 0, 1],
      [2, 0, 1, 2, 0, 0, 1, 0, 0, 0],
      [0, 2, 0, 0, 2, 0, 0, 0, 0, 2],
      [2, 0, 1, 0, 0, 0, 0, 0, 2, 0],
      [0, 0, 2, 0, 2, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 2, 0, 0, 0, 1, 2],
      [0, 0, 2, 0, 2, 0, 0, 0, 0, 0],
      [0, 2, 0, 0, 0, 0, 2, 0, 1, 0],
      [1, 1, 0, 1, 0, 2, 0, 0, 0, 2]]


def binairo(board):
    def binairoHelper(board, x, y):
        if x == len(board):
            return binairoHelper(board, 0, y + 1)
        if y == len(board):
            return board
        
        if board[y][x] != 0:
            return binairoHelper(board, x + 1, y)
        
        for i in range(1, 3):
            board[y][x] = i
            if not valid(board, x, y):
                continue
            ret = binairoHelper(board, x + 1, y)
            if ret:
                return ret

        board[y][x] = 0
        return False
    
    def valid(board, x, y):
        # more than 2 in a row
        for offset in range(-2, 1):
            if x + offset < 0 or x + offset + 2 >= len(board):
                continue
            if board[y][x + offset] == board[y][x + offset + 1] and board[y][x + offset] == board[y][x + offset + 2]:
                return False
            
        # more than 2 in a column
        for offset in range(-2, 1):
            if y + offset < 0 or y + offset + 2 >= len(board):
                continue
            if board[y + offset][x] == board[y + offset + 1][x] and board[y + offset][x] == board[y + offset + 2][x]:
                return False
            
        # more than n/2 in a row
        if board[y].count(1) > len(board) / 2 or board[y].count(2) > len(board) / 2:
            return False
        
        # more than n/2 in a column
        col = [board[i][x] for i in range(len(board))]
        if col.count(1) > len(board) / 2 or col.count(2) > len(board) / 2:
            return False
        
        return True
    
    return binairoHelper(board, 0, 0)

res = binairo(B1)
print("\n".join([" ".join([f"{x:>3}" for x in row]) for row in res]))