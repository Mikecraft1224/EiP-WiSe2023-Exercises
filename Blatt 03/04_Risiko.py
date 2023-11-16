redWins = 0
blueWins = 0
draw = 0

for r1 in range(1,7):
    for r2 in range(1,7):
        for r3 in range(1,7):
            for b1 in range(1,7):
                for b2 in range(1,7):
                    r = sorted([r1,r2,r3], reverse=True)
                    b = sorted([b1,b2], reverse=True)

                    if r[0] > b[0] and r[1] > b[1]:
                        redWins += 1
                    elif r[0] <= b[0] and r[1] <= b[1]:
                        blueWins += 1
                    else:
                        draw += 1

print(f"Rot gewinnt: {redWins} mal\nBlau gewinnt: {blueWins} mal\nUnentschieden: {draw} mal")