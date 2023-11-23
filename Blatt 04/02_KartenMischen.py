import random
p = ['Kreuz','Pik','Herz','Karo']

search = ["Karo", "Pik", "Kreuz", "Herz"]
found = 0

for _ in range(1_000_000):
    for i in range(3,0,-1):
        j = random.randint(0,i)
        tmp = p[i]
        p[i] = p[j]
        p[j] = tmp

    if p == search:
        found += 1

print(f"Found {found} times ({found/1_000_000*100:.4f}%)")
print(f"Expected {1/24*100:.4f}%")

