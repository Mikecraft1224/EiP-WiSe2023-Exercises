# 1.
# Vom i-ten Spieltag zum i+1-ten Spieltag kommt man durch Rotation gegen den Uhrzeigersinn um 1 Feld und Umkehrung des Pfeiles an der 9.
# Die 9 spielt immmer mit dem Team, das die Spieltagsnummer i hat. 
# Bei den restlichen 8 gilt: (Nummer Team + Nummer Gegner) mod 9 = 2i mod 9.
# Für die Spiele mit 9 gilt: i mod 2 = 0 hat 9 Heimspiel, sonst hat 9 Gastspiel. 
# Bei den restlichen gilt: Wenn (Teamnummer + 9 - Spieltagsnummer) mod 9 mod 2 = 1, hat das Team ein Gastspiel, sonst Heimspiel


# 2.
with open("Blatt 05/Bundesliga-Klubs.txt", encoding="utf-8") as f:
    teams = [line.strip() for line in f.readlines()]


# l = [0, 1, 2, 4, 5, 6]
# l[-1] = 6
# l[1] = 1; l[-1 - 1] = 5
# l[2] = 2; l[-1 - 2] = 4

for day in range(len(teams) - 1):
    print("Spieltag", day + 1)

    j = len(teams) - 1
    for i in range(len(teams) // 2):
        if i == 0:
            if day % 2 == 0:
                print(f"{teams[-1]} -> {teams[0]}")
            else:
                print(f"{teams[0]} -> {teams[-1]}")
        else:
            if i % 2 == 0:
                # print(f"{teams[j]} -> {teams[i]}")
                print(f"{teams[-1 - i]} -> {teams[i]}")
            else:
                # print(f"{teams[i]} -> {teams[j]}")
                print(f"{teams[i]} -> {teams[-1 - i]}")

        j -= 1
    
    teams = [teams[-2]] + teams[:-2] + [teams[-1]]
    print()