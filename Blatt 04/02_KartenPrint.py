import random

farbe = [0x1f0d0,0x1f0a0,0x1f0b0,0x1f0c0]
rang = [11,1,14,13,10,9,8,7]

# Karten generieren
cards = [c + r for c in farbe for r in rang]
# cards = []
# for c in farbe:
#     for r in rang:
#         cards.append(c+r)

# Mischen
for i in range(len(cards) - 1, 0, -1):
    j = random.randint(0, i)
    cards[i], cards[j] = cards[j], cards[i]

# Ausgeben
players = [cards[:10], cards[10:20], cards[20:30]]
skat = cards[30:]

# player = players[i]
for i, player in enumerate(players):
    # print(f"({i}, {player})")
    print(f"Player {i+1}: ", end="")

    for f in farbe:
        for r in rang:
            if f+r in player:
                print(chr(f+r), end='')

    # for card in player:
    #     print(chr(card), end='')
    print()

print("Skat: ", end="")
for card in skat:
    print(chr(card), end='')
print()

# for f in farbe:
#     for r in rang:
#         print(chr(f+r),end='')
#     print()
# print(chr(0x1f0a0))
