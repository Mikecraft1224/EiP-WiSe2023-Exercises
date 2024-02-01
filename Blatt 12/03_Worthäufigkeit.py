# 3.1
with open("Blatt 12/Goethe.txt", "r", encoding="utf-8") as f:
    words = []

    for line in f.readlines()[26:1430]:
        for word in line.strip().split():
            word = word.lower().strip(".,;:!?")
            if word != "": # and not word.isnumeric():
                words.append(word)

# 3.2
common = {}
for word in words:
    if word not in common:
        common[word] = 0
    common[word] += 1

# print(common.items())
top100 = dict(sorted(list(common.items()), \
            key=lambda x: x[1], reverse=True)[:100])
print(top100)

# 3.3
# Statt einem Dictionary müsste man eine Liste aus Tupeln benutzen
# [(word, count), ...]
# Allerdings wäre das deutlich ineffizienter, da man durch die ganze Liste 
# iterieren müsste, um ein bestimmtes Wort zu finden.