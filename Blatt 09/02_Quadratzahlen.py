import itertools
import random

A = [8,1,15,10,6,3,13,12,4,5,11,14,2,7,9]
random.shuffle(A)

def squareNumberList(l):
    for permutation in itertools.permutations(l):
        for i in range(1, len(permutation)):
            if (permutation[i-1] + permutation[i])**0.5 % 1 != 0:
                break
        else:
            return list(permutation)
        
# print(squareNumberList(A))
        
def fastSquareNumberList(l):
    def fastSquareNumberListHelper(l, remaining: list):
        if not remaining:
            return l
        
        for e in remaining:
            if (l[-1] + e)**0.5 % 1 != 0:
                continue
            remaining.remove(e)
            ret = fastSquareNumberListHelper(l + [e], remaining)
            if ret:
                return ret
            remaining.append(e)
        return False
    
    for e in l:
        remaining = l.copy()
        remaining.remove(e)
        ret = fastSquareNumberListHelper([e], remaining)
        if ret:
            return ret
    return False

# print(fastSquareNumberList(A))

# Bonus

def adjacencyList(l):
    adjacency = {}.fromkeys(l, [])
    for e1 in l:
        for e2 in l:
            if e1 == e2:
                continue
            if (e1 + e2)**0.5 % 1 == 0:
                adjacency[e1] = adjacency[e1] + [e2]
    return adjacency

def hamiltonPath(adjl):
    def hamiltonPathHelper(adjl, path):
        if len(path) == len(adjl):
            return path
        
        for e in adjl[path[-1]]:
            if e in path:
                continue
            ret = hamiltonPathHelper(adjl, path + [e])
            if ret:
                return ret
        return False

    for e in adjl:
        ret = hamiltonPathHelper(adjl, [e])
        if ret:
            return ret
    return False

print(hamiltonPath(adjacencyList(A)))