import random

def readAndSplit(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip().split()
        return lines
    
def scramble(word):
    if len(word) <= 5 or (len(word) == 6 and word[-1] in ".,;:!?"):
        return word

    word = list(word)
    toRerange = word[2:-3] if word[-1] in ".,;:!?" else word[2:-2]
    random.shuffle(toRerange)
    
    if word[-1] in ".,;:!?":
        word[2:-3] = toRerange
    else:
        word[2:-2] = toRerange
    
    return "".join(word)


def scrambleText(words):
    for i in range(len(words)):
        for j in range(len(words[i])):
            words[i][j] = scramble(words[i][j])
    return words

    
if __name__ == '__main__':
    words = readAndSplit("Blatt 06/JGU.txt")

    words = scrambleText(words)
    words = "\n".join([" ".join(line) for line in words])
    print(words)