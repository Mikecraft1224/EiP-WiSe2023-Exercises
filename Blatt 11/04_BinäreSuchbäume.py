# Die Klasse Baumknoten dient zur Repräsentation eines Knotens eines
# binären Suchbaumes. Ein binärer Suchbaum hat die Eigenschaft, dass
# alle Schlüsseleinträge im linken Unterbaum eines Knotens kleiner
# (oder gleich) als der Schlüssel des betrachteten Knotens sind und alle
# Schlüssel des rechten Unterbaums größer als dieser Schlüssel sind.
# Mit Hilfe der Memberfunktionen dieser Klasse kann der Unterbaum
# unterhalb eines Baumknotens zu verschiedenen Zwecken durchmustert werden.

class Baumknoten:
    # Ein Knoten des Suchbaumes beinhaltet einen Schlüssel und den damit
    # verbundenen Inhalt. Desweiteren zwei Verweise auf die (Wurzel)Knoten
    # des linken und rechten Teilbaumes.
    def __init__(self,schluessel,inhalt):
        self.schluessel = schluessel
        self.inhalt = inhalt
        self.links = self.rechts = None

    # Eine Memberfunktion zum Einfügen eines neuen Baumknotens (knoten).
    def einfuege(self,knoten):
        # Wenn der Schlüssel des einzufügenden Knotens gleich dem Schlüssel
        # des betrachteten Baumknotens (self) ist,
        if knoten.schluessel == self.schluessel:
            # überschreiben wir den alten Inhalt mit dem neuen.
            self.inhalt = knoten.inhalt
            return
        # Wenn der Schlüssel des einzufügenden Knotens kleiner ist als der Schlüssel
        # des betrachteten Baumknotens (self), verzweigen wir in den linken Unterbaum.
        if knoten.schluessel < self.schluessel:
            if self.links == None:
                # Wenn der linke Kindknoten nicht existiert, können wir dort den neuen
                # Knoten einfügen.
                self.links = knoten
            else:
                # Wenn der linke Kindknoten existiert, delegieren wir die Einfügeoperation
                # an diesen Knoten (self.links) durch einen rekursiven Aufruf.
                self.links.einfuege(knoten)
        else: # Analog für den rechten Unterbaum
            if self.rechts == None:
                self.rechts = knoten
            else:
                self.rechts.einfuege(knoten)

    # Eine Memberfunktion zum Suchen eines Knotens mit dem Schlüssel schluessel.
    def suche(self,schluessel):
        # 4.1
        node = self

        while node != None:
            if node.schluessel == schluessel:
                return node
            if schluessel < node.schluessel:
                node = node.links
            else:
                node = node.rechts
        return None

        # if schluessel == self.schluessel:
        #     return(self.inhalt)
        # if schluessel < self.schluessel:
        #     if self.links == None:
        #         return(None)
        #     return(self.links.suche(schluessel))
        # else:
        #     if self.rechts == None:
        #         return(None)
        #     return(self.rechts.suche(schluessel))

    # Erzeuge eine Zeichenkette für alle Schlüssel des Unterbaumes unterhalb des
    # aktuellen Knotens in sortierter Reihenfolge (Inorder).
    def __str__(self):
        s = ''
        # Wenn ein linker Unterbaum existiert, erzeugen wir eine sortierte Ausgabe
        # für alle Schlüssel in diesem Teilbaum.
        if self.links != None:
            s += str(self.links)
        # Dann geben wir den Schlüssel des betrachteten Knotens (self) aus.
        s += str(self.schluessel)+' '
        # Anschließend die Schlüssel im rechten Unterbaum, sofern dieser existiert.
        if self.rechts != None:
            s += str(self.rechts)
        return(s)

# Die Klasse Suchbaum stellt eine abstrakte Datenstruktur dar, mit der es möglich
# ist eine Menge von (Schlüssel,Inhalt)-Paaren effizient zu verwalten, so dass man
# leicht neue Einträge hinzufügen (und auch löschen kann - wie ???) und nach Einträgen
# mit einem bestimmten Suchschlüssel suchen kann. Diese Operationen benötigen nur
# so viele Schritte, wie der Suchbaum tief ist. (Bei einem gut balancierten Baum
# wächst die Tiefe nur logarithmisch mit der Knotenzahl.)
class Suchbaum:
    # Konstruktor für den leeren Suchbaum.
    def __init__(self):
        self.wurzel = None

    # Einfügen eines neuen (Schlüssel,Inhalt)-Paares.
    def einfuege(self,schluessel,inhalt):
        knoten = Baumknoten(schluessel,inhalt)
        if self.wurzel == None:
            self.wurzel = knoten
        self.wurzel.einfuege(knoten)

    # Suche nach einem Baumknoten, dessen Schlüssel dem Suchschlüssel entspricht.
    def suche(self,schluessel):
        if self.wurzel == None:
            return(None)
        return(self.wurzel.suche(schluessel))

    # Überladen der str-Funktion zur sortierten Ausgabe des gesamten Suchbaumes.
    def __str__(self):
        if self.wurzel == None:
            return('')
        # Wir deligieren die Arbeit an den Baumknoten wurzel.
        return(str(self.wurzel))
    
    # 4.2
    def __getitem__(self, key):
        return self.suche(key).inhalt
    
    def __setitem__(self, key, value):
        self.suche(key).inhalt = value

    # 4.3
    def first(self):
        node = self.wurzel
        while node.links != None:
            node = node.links
        return node.inhalt
    
    # 4.6
    def loesche(self, key):
        x = self.suche(key)
        y = x.rechts
        while y.links != None:
            y = y.links

        x.schluessel = y.schluessel
        x.inhalt = y.inhalt

        start = x.rechts
        if start != None:
            if start.links.schluessel == y.schluessel:
                start.links = y.rechts

# 4.4
# Um das nächstgrößere Element zu finden, müssen wir vom Knoten aus nach rechts gehen und 
# dann so weit wie möglich nach links. Wenn der Knoten keine rechten Kinder hat, müssen wir
# nach oben gehen, bis wir einen Knoten finden, der größer ist als der aktuelle Knoten.

# 4.5 
# Um einen Knoten zu löschen, suchen wir als erstes den nächsten Knoten, der größer ist als
# der zu löschende Knoten. 
# Falls dieser aus dem rechten Unterbaum kommt, müssen wir den rechten Unterbaum des zu löschenden
# Knotens an den neuen Knoten hängen und einen möglichen rechten Unterbaum des neuen Knotens an
# dessen Elternknoten hängen.
# Falls der Knoten keinen rechten Unterbaum hat, müssen wir den linken Unterbaum des zu löschenden
# Knotens an dessen Elternknoten hängen.

L = [25,34,27,12,38,18,10,21,46,5,14,20,15,35,23,8,42]

S = Suchbaum()
for x in L:
    S.einfuege(x,x)
print(S)

print(S.suche(44))