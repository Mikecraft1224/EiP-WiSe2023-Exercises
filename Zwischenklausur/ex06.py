def pangram(satz):
    # Effiziente Variante
    # for i in range(97, 123):
    #     if chr(i) not in satz:
    #         return False
    # return True

    # Einfache Variante
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in satz:
            return False
    return True
    