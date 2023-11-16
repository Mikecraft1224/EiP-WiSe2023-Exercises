import math

# count = 0

# c = 5
# while c < 20:
#     a = 1
#     while a < c:
#         b = a+1
#         while b < c:
#             if a*a+b*b == c*c:
#                 count += 1
#             b += 1
#         a += 1
#     c += 1

# print(count)

count = 0

for a in range(1, 1000):
    for b in range(a, 1000):
        c = math.sqrt(a*a+b*b)
        if c == int(c) and c < 1000:
            count += 1

print(count)

