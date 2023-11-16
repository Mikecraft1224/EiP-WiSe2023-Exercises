import random

r1 = random.randint(1,6)
r2 = random.randint(1,6)
r3 = random.randint(1,6)
print(r1,r2,r3)

b1 = random.randint(1,6)
b2 = random.randint(1,6)
print(b1,b2)

redPoints = 0
bluePoints = 0

r = sorted([r1,r2,r3], reverse=True)
b = sorted([b1,b2], reverse=True)

for i in range(2):
    if r[i] > b[i]:
        redPoints += 1
    else:
        bluePoints += 1

print(f"Rot: {redPoints} Punkte")
print(f"Blau: {bluePoints} Punkte")