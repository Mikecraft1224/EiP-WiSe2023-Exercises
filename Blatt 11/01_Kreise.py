# 1.1
# Der maximale Abstand zwischen den Mittelpunkten sodass die Kreise sich dennoch berühren ist
# der Radius der beiden Kreise addiert. Wenn der Abstand also kleiner oder gleich der Summe der
# Radien ist, berühren sich die Kreise oder schneiden sich. Wenn der Abstand größer ist, schneiden
# sich die Kreise nicht.
# Eine Kreisscheibe Ki liegt genau dann vollständig in der Kreisscheibe Kj, wenn der Abstand der
# Mittelpunkte addiert mit dem Radius von Ki kleiner oder gleich dem Radius von Kj ist.

# 1.2
class Kreis:
    def __init__(self, x0, y0, r) -> None:
        self.x0 = x0
        self.y0 = y0
        self.r = r

    def __str__(self) -> str:
        return f"Circle at ({self.x0}, {self.y0}) with radius {self.r}"
    
    def __repr__(self) -> str:
        return f"Circle({self.x0}, {self.y0}, {self.r})"

    def __contains__(self, other: 'Kreis') -> bool:
        return (self.x0 - other.x0)**2 + (self.y0 - other.y0)**2 + other.r**2 <= self.r**2
    
    def schneidet(self, other: 'Kreis') -> bool:
        return (self.x0 - other.x0)**2 + (self.y0 - other.y0)**2 <= (self.r + other.r)**2

    # 1.3
    def __lt__(self, other: 'Kreis'):
        return self.r < other.r

def sortieren(K: list[Kreis]) -> list[Kreis]:
    return sorted(K)

# 1.4
def enthaelt(K: list[Kreis]) -> list[list[bool]]:
    return [[k1 in k2 for k1 in K] for k2 in K]

K1 = Kreis(14,3,2)
K2 = Kreis(10,13,3)
K3 = Kreis(8,12,6)
K4 = Kreis(5,5,4)

# print(K1)
# print(K1 in K3)
# print(K2 in K3)
# print(K2.schneidet(K3))
# print(K4.schneidet(K3))

# cs = [K1, K2, K3, K4]

# print(cs)
# print(sortieren(cs))
# print(enthaelt(cs))