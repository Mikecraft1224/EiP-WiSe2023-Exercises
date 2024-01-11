import random

def recBackpacking(i, G):
    def recBackpackingHelper(i, G):
        if i == 0 or G == 0:
            return 0
        elif Gewicht[i-1] > G:
            return recBackpackingHelper(i-1, G)
        else:
            return max(recBackpackingHelper(i-1, G), Wert[i-1] + recBackpackingHelper(i-1, G-Gewicht[i-1]))
    return recBackpackingHelper(i, G)

def recBackpackingMemo(i, G):
    def recBackpackingMemoHelper(i, G):
        if i == 0 or G == 0:
            return 0
        elif Gewicht[i-1] > G:
            if memo[i][G] == -1:
                memo[i][G] = recBackpackingMemoHelper(i-1, G)
            return memo[i][G]
        else:
            if memo[i][G] == -1:
                memo[i][G] = max(recBackpackingMemoHelper(i-1, G), Wert[i-1] + recBackpackingMemoHelper(i-1, G-Gewicht[i-1]))
            return memo[i][G]
        
    memo = [[-1 for j in range(G+1)] for i in range(n+1)]
    return recBackpackingMemoHelper(i, G)

def iterBackpacking(G):
    memo = [[0 for i in range(G + 1)] for j in range(n + 1)]
    # TODO explain this zeilenweise
    for i in range(1, n + 1):
        for j in range(1, G + 1):
            if Gewicht[i-1] > j:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = max(memo[i-1][j], Wert[i-1] + memo[i-1][j-Gewicht[i-1]])

    # print("\n".join([" ".join([f"{i:>2}" for i in row]) for row in memo]))
                
    return memo[n][G]

def iterBackpackingTraceback(G):
    memo = [[0 for i in range(G + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, G + 1):
            if Gewicht[i-1] > j:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = max(memo[i-1][j], Wert[i-1] + memo[i-1][j-Gewicht[i-1]])
    
    elements = []

    i = n
    j = G
    while i > 0 and j > 0:
        if memo[i][j] != memo[i-1][j]:
            elements.append(i)
            j -= Gewicht[i-1]
        i -= 1
    elements.reverse()
    return elements, memo[n][G]

random.seed(4242)

n = 22
Gewicht = [random.randint(20,100) for i in range(n)]
Wert = [random.randint(20,100) for i in range(n)]
print(f"n: {n}")
print(f"weights: {Gewicht}")
print(f"values: {Wert}\n")

recBackpacking(n, 500)
recBackpackingMemo(n, 500)
iterBackpacking(500)
iterBackpackingTraceback(500)