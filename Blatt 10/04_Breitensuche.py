class Schlange:
    def __init__(self) -> None:
        self.schlange = []

    def hinten_an_die_Schlange_anfuegen(self, element):
        self.schlange.append(element)

    def vorderstes_Element_der_Schlange(self):
        return self.schlange[0]
    
    def vorderstes_Element_der_Schlange_ausgeben_und_entfernen(self):
        return self.schlange.pop(0)
    
    def ist_Schlange_leer(self):
        return len(self.schlange) == 0
    

class Graph:
    def __init__(self, dateiname) -> None:
        with open(dateiname, "r") as f:
            lines = f.readlines()
            splitted = [line.split() for line in lines]
            
            self.G = [[] for _ in range(int(splitted[0][0]) + 1)]
            
            for line in splitted[1:]:
                u = int(line[0])
                v = int(line[1])
                self.G[u].append(v)
                self.G[v].append(u)
            
    def ausgabe_der_Adjazenzlisten(self):
        for i in range(len(self.G)):
            print(i, self.G[i])

    def breitenSuche(self, startKnoten):
        schlange = Schlange()
        besucht = [False for _ in range(len(self.G))]
        pred = [None for _ in range(len(self.G))]

        schlange.hinten_an_die_Schlange_anfuegen(startKnoten)
        besucht[startKnoten] = True

        while not schlange.ist_Schlange_leer():
            u = schlange.vorderstes_Element_der_Schlange_ausgeben_und_entfernen()
            for v in self.G[u]:
                if not besucht[v]:
                    schlange.hinten_an_die_Schlange_anfuegen(v)
                    besucht[v] = True
                    pred[v] = u

        return pred
    
    def ausgabe_des_kuerzesten_Weges(self, startKnoten, zielKnoten):
        pred = self.breitenSuche(startKnoten)
        u = zielKnoten
        weg = []

        while u != startKnoten:
            weg.append(u)
            u = pred[u]

        weg.append(startKnoten)
        weg.reverse()
        return weg


graph = Graph("Blatt 10/huepfburg0.txt")
# graph.ausgabe_der_Adjazenzlisten()
# print(graph.breitenSuche(1))
print(graph.ausgabe_des_kuerzesten_Weges(1, 2))