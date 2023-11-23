import random

# numbers = []
# while len(numbers) < 6:
#     n = random.randint(1, 49)
#     if n not in numbers:
#         numbers.append(n)

# allNumbers = list(range(1, 50))
# numbers = []
# for i in range(6):
#     # n = random.choice(allNumbers)
#     j = random.randint(0, len(allNumbers) - 1)
#     n = allNumbers[j]
#     numbers.append(n)
#     allNumbers.remove(n)

choice = [2, 5, 23, 34, 42, 45]

numbers = sorted(random.sample(range(1, 50), 6))
for n in numbers:
    print(n, end=" ")
print()

# map(str, numbers) = [str(n) for n in numbers]
# "-".join(list) = list[0]-list[1]-...-list[n]
# print(" ".join(map(str, numbers)))

# print(f"Correct guesses: {sum([1 for n in numbers if n in choice])}")
correct = 0
for n in numbers:
    if n in choice:
        correct += 1
print(f"Correct guesses: {correct}")

