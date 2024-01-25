import random
import time

class Listenknoten:
    def __init__(self,inhalt):
        self.inhalt = inhalt
        self.next = None

class Liste:
    def __init__(self):
        self.kopf = None

    def einfuege(self,inhalt):
        knoten = Listenknoten(inhalt)
        knoten.next = self.kopf
        self.kopf = knoten

    def suche(self,element, moveToFront = False):
        last = None
        scndlast = None
        knoten = self.kopf
        while knoten != None:
            if knoten.inhalt == element:
                # 2.1 Move to Front
                if last != None and moveToFront:
                    last.next = knoten.next
                    knoten.next = self.kopf
                    self.kopf = knoten

                # 2.2 Transpose
                if last != None and not moveToFront:
                    if scndlast != None:
                        scndlast.next = knoten
                    else: 
                        self.kopf = knoten
                    last.next = knoten.next
                    knoten.next = last

                return(True)
            scndlast = last
            last = knoten
            knoten = knoten.next
        return(False)

    def __str__(self):
        s = ''
        knoten = self.kopf
        while knoten != None:
            s += str(knoten.inhalt)+' '
            knoten = knoten.next
        return(s)

def createList(n):
    L = Liste()
    for i in range(n):
        L.einfuege(i)
    return L


# 2.3
for exp in range(1, 8):
    n = 10**exp

    print(f"\nn = {n}")

    L = createList(100)
    start = time.time()
    for i in range(n):
        L.suche(int(random.triangular(0,100,0)), True)
    end = time.time()
    print(f"Move to Front: {end - start:.4f}s")

    L = createList(100)
    start = time.time()
    for i in range(n):
        L.suche(int(random.triangular(0,100,0)), False)
    end = time.time()
    print(f"Transpose: {end - start:.4f}s")


# for i in range(20):
#     x = int(random.triangular(0,100,0))
#     print('suche Element '+str(x))
