# 1.
a = [i for i in range(10)]

for i in range(len(a)//2):
    # a[i], a[-i-1] = a[-i-1], a[i]
    a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]

# print(a)

# 2.
b = [i for i in range(10)]
# fst = b.pop(0)
# b.append(fst)

# b.append(b.pop(0))

fst = b[0]
for i in range(len(b)-1):
    b[i] = b[i+1]
b[-1] = fst

print(b)

# b[1:3]