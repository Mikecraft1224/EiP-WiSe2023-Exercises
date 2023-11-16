import random

# w1 = random.randint(1,6)
# w2 = random.randint(1,6)
# w3 = random.randint(1,6)

def hausnummer(w1, w2, w3):
    h, z, e = 0, 0, 0

    # 1. Wurf
    if w1 >= 5:
        h = w1
    elif w1 >= 3:
        z = w1
    else:
        e = w1

    # 2. Wurf
    if w2 >= 3 and h == 0:
        h = w2
    elif w2 >= 3 or e != 0:
        z = w2
    else:
        e = w2

    # if w2 >= 3:
    #     if h == 0:
    #         h = w2
    #     else:
    #         z = w2
    # else:
    #     if e == 0:
    #         e = w2
    #     else:
    #         z = w2

    # 3. Wurf
    if h == 0:
        h = w3
    elif z == 0:
        z = w3
    else:
        e = w3

    # print(f"Hausnummer: {h}{z}{e}")

    return 100*h + 10*z + e

summe = 0
i = 0

for w1 in range(1, 7):
    for w2 in range(1, 7):
        for w3 in range(1, 7):
            summe += hausnummer(w1, w2, w3)
            i += 1

print(f"Erwartungswert: {summe/i:.0f}")