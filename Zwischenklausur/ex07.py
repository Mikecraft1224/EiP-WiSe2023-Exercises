# Im Prinzip die Fibonacci-Folge mit 1 und 2 als Startwerten
def zahlDerSchrittfolgen(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return zahlDerSchrittfolgen(n-1) + zahlDerSchrittfolgen(n-2)

    # Oder:
    # a, b = 1, 2
    # for i in range(n-1):
    #     a, b = b, a+b
    # return a