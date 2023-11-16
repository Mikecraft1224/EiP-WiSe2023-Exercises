import math

K0 = float(input('K0 ='))
K  = float(input('K  ='))
p  = float(input('p  ='))

n = math.log(K/K0, 1+p)
# n = math.log(K/K0) / math.log(1+p)

print(f'n = {n}')
