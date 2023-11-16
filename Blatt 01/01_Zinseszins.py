# Zinseszins-Rechner

Startkapital = float(input('Geben Sie das Startkapital ein: '))
Zinssatz = float(input('Geben Sie den Zinssatz ein: '))
Jahre = int(input('Geben Sie die Anzahl der Jahre ein: '))

# Lesen Sie hier zusaetzlich den Zinssatz und die Anzahl der Jahre ein.

Endkapital = Startkapital * (1 + Zinssatz) ** Jahre

# Geben Sie hier zusaetzlich den eingelesenen Zinssatz und die 
# eingelesene Anzahl der Jahre aus.

# Berechnen Sie anschliessend das Kapital mit Zins und Zinseszins 
# nach der Laufzeit und geben Sie das Ergebnis aus.
# Zum Potenzieren verwenden Sie bitte den ** Operator, 
# z.B. 3 hoch 2 laesst sich in Python als 3 ** 2 berechnen.

print(f'Das Endkapital betraegt {Endkapital:.2f}€ nach {Jahre} Jahren.')