class Bruch:
    def __init__(self,zaehler,nenner = 1):
        self.z = zaehler
        self.n = nenner

    def __add__(self, other):
        ergebnis_zaehler = self.z * other.n + self.n * other.z
        ergebnis_nenner = self.n * other.n
        return(Bruch(ergebnis_zaehler,ergebnis_nenner).reduce())

    def __sub__(self, other):
        ergebnis_zaehler = self.z * other.n - self.n * other.z
        ergebnis_nenner = self.n * other.n
        return(Bruch(ergebnis_zaehler,ergebnis_nenner).reduce())

    def __mul__(self, other):
        ergebnis_zaehler = self.z * other.z
        ergebnis_nenner = self.n * other.n
        return(Bruch(ergebnis_zaehler,ergebnis_nenner).reduce())

    def __truediv__(self, other):
        ergebnis_zaehler = self.z * other.n
        ergebnis_nenner = self.n * other.z
        return(Bruch(ergebnis_zaehler,ergebnis_nenner).reduce())

    def __neg__(self):
        return(Bruch(-self.z,self.n))

    def __str__(self):
        if self.n == 1:
            return(str(self.z))
        return(str(self.z)+'/'+str(self.n))
    
    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        if self.n * other.n > 0:
            return(self.z * other.n < self.n * other.z)
        else:
            return (self.z * other.n > self.n * other.z)

    def __eq__(self, other):
            return(self.z * other.n == self.n * other.z)

    def reduce(self):
        g = Bruch.ggT(self.z,self.n)
        return(Bruch(self.z // g,self.n // g))

    def ggT(a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return(a)

class Vektor:
    def __init__(self,*v):
        self.v = [Bruch(x) for x in v]

    def __getitem__(self, i):
        return(self.v[i])
    
    def __setitem__(self, i, value):
        self.v[i] = value

    def __add__(self, other):
        return Vektor(*[self.v[i] + other.v[i] for i in range(len(self.v))])
    
    def __sub__(self, other):
        return Vektor(*[self.v[i] - other.v[i] for i in range(len(self.v))])
    
    def __mul__(self, other):
        return Vektor(*[self.v[i] * other for i in range(len(self.v))])
    
    def __truediv__(self, other):
        return Vektor(*[self.v[i] / other for i in range(len(self.v))])
    
    def Skalarprodukt(self, other):
        return sum([self.v[i] * other.v[i] for i in range(len(self.v))])
    
    def __str__(self):
        return str(self.v)      # needs __repr__ in Bruch
    

L = (1,2,3)
a = Vektor(*L)
b = Vektor(4,5,6)

print(a+b)
print(Vektor.Skalarprodukt(a/4+b*3,a*2+b/5))

a[1] = 0        # a.__setitem__(1,0)
print(a[1])     # a.__getitem__(1)