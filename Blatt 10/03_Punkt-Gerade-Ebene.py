import math

def Skalarprodukt(a,b):
    return(a.x*b.x+a.y*b.y+a.z*b.z)

class Punkt:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Punkt"):
        return Punkt(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: "Punkt"):
        return Punkt(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return Punkt(self.x * other, self.y * other, self.z * other)
    
    def __truediv__(self, other):
        return Punkt(self.x / other, self.y / other, self.z / other)
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
class Gerade:
    def __init__(self, a, b):
        self.a = a
        self.b = b - a

    def __str__(self):
        return f"{self.a} + r * {self.b}"

class Ebene:
    def __init__(self, nx, ny, nz, d):
        self.n = Punkt(nx, ny, nz)
        self.d = d

    def ist_senkrecht_zu(self, g: Gerade):
        return g.b.x / self.n.x == g.b.y / self.n.y == g.b.z / self.n.z
    
    def schneide(self, g: Gerade):
        # nx * (ax + r * bx) + ny * (ay + r * by) + nz * (az + r * bz) = d
        # r = (d - nx * ax - ny * ay - nz * az) / (nx * bx + ny * by + nz * bz)
        # nx * ax + ny * ay + nz * az: Skalarprodukt(n, a)
        # nx * bx + ny * by + nz * bz: Skalarprodukt(n, b)
        r = (self.d - Skalarprodukt(self.n, g.a)) / Skalarprodukt(self.n, g.b)
        return g.a + r * g.b
    
    def abstand(self, p: Punkt):
        upper = abs(Skalarprodukt(self.n, p) - self.d)
        lower = math.sqrt(Skalarprodukt(self.n, self.n))
        return upper / lower
    
    def __str__(self):
        return f"{self.n.x}x + {self.n.y}y + {self.n.z}z = {self.d}"    


P = Punkt(1,0,2)
Q = Punkt(5,2,6)
g = Gerade(P,Q)
E = Ebene(2,1,2,6)

print(E.ist_senkrecht_zu(g))

M = (P+Q)/2
print(M)
normale = Q-P
d = Skalarprodukt(Q-P,M)

F = Ebene(normale.x,normale.y,normale.z,d)
print(F)
print(F.abstand(P),F.abstand(Q))
