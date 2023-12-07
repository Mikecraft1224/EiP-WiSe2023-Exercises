def loadAdjacencyList(file):
    with open(file, "r") as f:
        lines = f.readlines()
        n = int(lines[0].split()[0])
        adj = {i: [] for i in range(1, n+1)}
        # adj = [[] for i in range(n+1)]

        for line in lines[1:]:
            l = line.split()
            adj[int(l[0])].append(int(l[1]))
            adj[int(l[1])].append(int(l[0]))
        return(adj)
    

def distField(adj, s):
    dists = {i: None for i in adj}
    dists[s] = 0

    queue = [s]

    while len(queue) > 0:   # while queue:
        v = queue.pop(0)
        for w in adj[v]:
            if dists[w] is None:
                dists[w] = dists[v] + 1
                queue.append(w)
    
    return dists

def distField2D(adj):
    dists = {i: None for i in adj}

    for s in adj:
        dists[s] = distField(adj, s)

    return dists

def diameter(adj):
    dists = distField2D(adj)
    # return max([max(dists[s].values()) for s in dists])

    maxDist = 0
    for u in dists:
        for v in dists[u]:
            if dists[u][v] > maxDist:
                maxDist = dists[u][v]
    return maxDist


if __name__ == '__main__':
    # adj = loadAdjacencyList("Blatt 06/huepfburg0.txt")
    # dists = distField(adj, 1)
    # dists2D = distField2D(adj)
    # dia = diameter(adj)

    for i in range(5):
        adj = loadAdjacencyList(f"Blatt 06/huepfburg{i}.txt")
        dia = diameter(adj)
        print(f"dia: {dia} for huepfburg{i}.txt")