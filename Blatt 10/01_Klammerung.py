# 1.1
# Wenn eine neue Klammer geöffnet wird, wird diese in den Stapel gelegt, jedes Mal wenn eine geschlossen wird, wird eine entfernt. Falls der Stapel am Ende leer ist, ist die Klammerung korrekt.
# Ansonsten ist sie falsch.

# 1.2
class Stapel:
    def __init__(self):
        # first in first out
        self.stapel = []
    
    def push(self, element):
        self.stapel.append(element)

    def pop(self):
        self.stapel.pop()

    def peek(self):
        return self.stapel[-1]
        
    def isEmpty(self):
        return len(self.stapel) == 0
    
# 1.3
def ist_korrekt_geklammert(w):
    S = Stapel()
    for e in w:
        if e in "([":
            S.push(e)
        elif e in ")]":
            if S.isEmpty():
                return False
            if e == ")" and S.peek() == "(":
                S.pop()
            elif e == "]" and S.peek() == "[":
                S.pop()
            else:
                return False
    return S.isEmpty()