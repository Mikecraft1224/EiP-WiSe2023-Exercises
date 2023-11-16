l = 0.0
r = 2.0
eps = 1e-6


def f(x):
    return x**2 - 2

while r - l > eps:
    m = (l + r)/2

    if f(m) < 0:
        l = m
    else:
        r = m

print("Nullstelle: ", m)