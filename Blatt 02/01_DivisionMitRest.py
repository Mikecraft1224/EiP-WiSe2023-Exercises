jahr = int(input("Bitte geben Sie ein Jahr ein: "))

# if jahr%4 != 0:
#     print(f"{jahr} ist kein Schaltjahr.")
# elif jahr%100 != 0:
#     print(f"{jahr} ist ein Schaltjahr.")
# elif jahr%400 != 0:
#     print(f"{jahr} ist kein Schaltjahr.")
# else:
#     print(f"{jahr} ist ein Schaltjahr.")


if jahr%4 == 0:
    if jahr%100 == 0:
        if jahr%400 == 0:
            print(f"{jahr} ist ein Schaltjahr.")
        else:
            print(f"{jahr} ist kein Schaltjahr.")
    else:
        print(f"{jahr} ist ein Schaltjahr.")
else:
    print(f"{jahr} ist kein Schaltjahr.")