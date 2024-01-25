class Frau:
    def __init__(self,name):
        self.name = name
        self.mutter = None
        self.kinder = []
        self.markiert = False

class Ahnentafel:
    def __init__(self,ahnentafel):
        datei = open(ahnentafel,'r')

        zeile = datei.readline()
        n = int(zeile)

        self.F = [Frau(i+1) for i in range(n)]

        for zeile in datei:
            s = zeile.split()
            kind = int(s[0])
            mutter = int(s[1])
            self.F[kind-1].mutter = self.F[mutter-1]

            # 3.2
            self.F[mutter-1].kinder.append(self.F[kind-1])
        datei.close()

    # 3.3
    def anzahlMutanten(self):
        count = 0
        for f in self.F:
            if f.mutter == None:
                count += 1
        return count
        # return len([f for f in self.F if f.mutter == None])
    
    # 3.4
    def zahlDerNachkommen(self, f):
        count = 0
        for k in self.F[f-1].kinder:
            count += 1 + self.zahlDerNachkommen(k.name)
        return count
    
    # 3.5
    def laengsteAhnenReihe(self):
        longest = 0
        for f in self.F:
            s = f
            count = 0

            while s != None:
                s = s.mutter
                count += 1
            
            longest = max(longest, count)
        return longest
    
    # 3.6
    def juengsteGemeinsameAhnin(self, f1, f2):
        s1 = self.F[f1-1]
        s2 = self.F[f2-1]
        youngest = None

        while s1 or s2:
            if s1 == s2:
                youngest = s1
                break
            if s1:
                s1 = s1.mutter
                if s1.markiert:
                    youngest = s1
                    break
                s1.markiert = True
            if s2:
                s2 = s2.mutter
                if s2.markiert:
                    youngest = s2
                    break
                s2.markiert = True

        # Reset
        for f in self.F:
            f.markiert = False

        return youngest.name
    

at = Ahnentafel("Blatt 11/Ahnen.txt")
print(f"Anzahl der Mutanten: {at.anzahlMutanten()}")
print(f"Anzahl der Nachkommen: {at.zahlDerNachkommen(1)}")
print(f"Längste Ahnenreihe: {at.laengsteAhnenReihe()}")
print(f"Jüngste gemeinsame Ahnin: {at.juengsteGemeinsameAhnin(30, 41)}")