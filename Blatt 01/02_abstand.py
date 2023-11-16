import math

ax = float(input('ax = '))
ay = float(input('ay = '))
bx = float(input('bx = '))
by = float(input('by = '))

dx = bx - ax
dy = by - ay

dist = math.sqrt(dx**2 + dy**2)

print(f"""Der Abstand zwischen den Punkten \
({ax}, {ay}) und ({bx}, {by}) beträgt {dist:.2f}.""")