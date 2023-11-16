import math

ax = 10.64
ay = 3.169
bx = -1.919
by = -8.44
cx = -3.92
cy = 9.569

# Erwartete Ausgabe 'AB' bzw. 'BC' bzw 'CA'
AB = math.sqrt((bx - ax)**2 + (by - ay)**2)
BC = math.sqrt((cx - bx)**2 + (cy - by)**2)
CA = math.sqrt((ax - cx)**2 + (ay - cy)**2)

if AB < BC and AB < CA:
    print('AB')
elif BC < AB and BC < CA:
    print('BC')
else:
    print('CA')

# print(sorted([(AB, 'AB'), (BC, 'BC'), (CA, 'CA')], key=lambda x: x[0])[0][1])