# 1


# 2
def iterPyramid(n):
    memo = [[0 for i in range(2*n + 1)] for j in range(n + 1)]
    memo[0][0] = 1

    for i in range(1, 2*n + 1):
        for j in range(n + 1):
            if (i + j)%2 == 1: # Skips not needed calculations
                continue

            if j > 0 and i == 0:
                memo[j][i] = 0
            elif j == 0 and i > 0:
                memo[j][i] = memo[1][i - 1]
            elif j == n: # Added to prevent out of bounds
                memo[j][i] = memo[j - 1][i - 1]
            else:
                memo[j][i] = memo[j - 1][i - 1] + memo[j + 1][i - 1]
    return memo[0][2*n]

# 5
n = 8

memo = [[-1 for i in range(2*n+1)] for j in range(n+1)]
# memo = {}

def recPyramid(j, i):
    if i == 0 and j == 0:
        return 1
    elif i == 0:
        return 0
    elif j == 0:
        if memo[j][i] == -1:
            memo[j][i] = recPyramid(1, i-1)
        return memo[j][i]
    # elif j == n:
    #     return recPyramid(j-1, i-1)
    else:
        if memo[j][i] == -1:
            memo[j][i] = recPyramid(j-1, i-1) + recPyramid(j+1, i-1)
        return memo[j][i]