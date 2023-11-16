import math

K0 = float(input('K0 ='))
K  = float(input('K  ='))
n  = float(input('n  ='))

p = (K/K0)**(1/n) - 1

print(f'p = {p}')
