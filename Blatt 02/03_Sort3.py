a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a < b:
    a,b = b,a
if a < c:
    a,c = c,a
if b < c:
    b,c = c,b

# 1.
# l = sorted([a, b, c])

# 2.
# l = [a, b, c]
# l.sort()

print(a,b,c)
