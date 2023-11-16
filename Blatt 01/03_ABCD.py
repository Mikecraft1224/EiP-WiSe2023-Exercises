import math

ax = int(10.64*1000)
ay = int(3.169*1000)
bx = int(-1.919*1000)
by = int(-8.44*1000)
cx = int(-3.92*1000)
cy = int(9.569*1000)

dx = int(1.0*1000)
dy = int(1.0*1000)

z = 1000

AD = math.sqrt((dx - ax)**2 + (dy - ay)**2)
BD = math.sqrt((dx - bx)**2 + (dy - by)**2)
CD = math.sqrt((dx - cx)**2 + (dy - cy)**2)

if AD == BD and BD == CD:
    print(f"Der Abstand ist zu jedem Punkt gleich mit der Distanz {AD/1000}.")
else:
    print("Die Kanten sind nicht gleich lang.")

