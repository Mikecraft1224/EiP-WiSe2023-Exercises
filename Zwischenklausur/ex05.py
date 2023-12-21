#1
def konvertiere(A, G):
    for j in range(len(A)):
        G.append([])
        for i in range(len(A)):
            if A[j][i]:
                G[j].append(i)
    return G

#2
def istZweiFaerbbar(G):
    faerbung = [0 for i in range(len(G))]

    queue = [(0, 1)]
    while len(queue) > 0:
        # Nimmt das erste Element aus der Queue
        node, color = queue.pop(0)

        # Wenn der Knoten schon gefärbt ist, aber nicht mit der richtigen Farbe, ist der Graph nicht 2-färbbar
        if faerbung[node] != 0 and faerbung[node] != color:
            return False
        faerbung[node] = color

        # Fügt alle Nachbarn des Knotens in die Queue ein und färbt sie mit der anderen Farbe
        for neighbor in G[node]:
            if faerbung[neighbor] == 0:
                queue.append((neighbor, -color))