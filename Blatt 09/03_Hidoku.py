H1 = [[ 0, 0, 0, 0, 0, 0],
      [ 0, 0,13, 5, 0, 0],
      [17, 0, 0, 0, 7, 8],
      [ 1, 0, 0,21,24, 0],
      [36,19,32, 0, 0, 0],
      [ 0, 0, 0,30,28, 0]]

H2 = [[ 0, 0, 3, 0, 1,64, 0,61],
      [ 7, 0, 0,12, 0, 0, 0,58],
      [ 0, 0, 9, 0, 0, 0, 0, 0],
      [47, 0, 0, 0,14, 0, 0,31],
      [45,18,17, 0, 0, 0, 0,33],
      [ 0, 0, 0, 0,52, 0, 0, 0],
      [ 0,21,42, 0, 0, 0, 0,36],
      [ 0, 0, 0,25,27, 0, 0, 0]]

H3 = [[42, 0,39, 0,36, 2, 0, 0,32, 0],
      [ 0,43,38, 0, 0, 0, 1,27, 0,30],
      [ 0,45,46, 5, 6, 8, 0, 0, 0, 0],
      [50, 0, 0, 0, 0,10, 0,24,25, 0],
      [ 0,53, 0,87, 0,11, 0, 0, 0,21],
      [ 0, 0, 0,88, 0,83, 0,15, 0, 0],
      [56,58, 0, 0,84, 0, 0,16, 0, 0],
      [ 0,94, 0, 0, 0, 0,81, 0, 0,76],
      [95, 0, 0,60,63, 0,67, 0, 0,74],
      [ 0,96,100,61,0,64, 0,69,71,73]]

# besonders schwierig
H4 = [[ 0, 0, 0, 0, 0, 0, 0, 0,48, 0],
      [0,100, 0, 0, 0,18, 0,47, 0, 0],
      [26, 0, 0, 0, 0, 0, 0,11, 0,13],
      [27, 0,29, 0, 0, 0, 0, 0, 0, 0],
      [ 0,59, 0, 0, 0, 0, 0, 0, 0, 0],
      [60, 0, 0, 0, 0, 0,93, 0, 0, 0],
      [ 0, 0,64, 0, 0, 0, 0, 0,41, 0],
      [ 4, 0,77,65, 0, 0, 0,86, 0, 0],
      [ 0, 0,74, 0, 0,67,81, 0, 0,37],
      [ 1, 0, 0,73,72, 0, 0, 0, 0, 0]]


def hidoku(board):
    preFilled = {
        e: (x, y) for y, l in enumerate(board)
            for x, e in enumerate(l) if e != 0
    }

    def hidokuHelper(board, n, x, y):
        if n == len(board) ** 2:
            return board
        
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board) or (nx, ny) == (x, y):
                    continue
                
                if not valid(board, n+1, nx, ny):
                    continue

                board[ny][nx] = n + 1
                ret = hidokuHelper(board, n + 1, nx, ny)
                if ret:
                    return ret
                if not (nx, ny) in preFilled.values():
                    board[ny][nx] = 0
        return False

    def valid(board, n, x, y):
        if n in preFilled and (x, y) != preFilled[n]:
            return False
        if not n in preFilled and (x, y) in preFilled.values():
            return False
        if board[y][x] != 0 and not n in preFilled:
            return False
        return True

    return hidokuHelper(board, 1, *preFilled[1])

solution = hidoku(H1)
print("\n".join([" ".join([f"{x:>3}" for x in y]) for y in solution]))