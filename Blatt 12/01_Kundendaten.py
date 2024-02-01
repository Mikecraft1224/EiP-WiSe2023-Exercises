import glob
import json

# 1.1
def sum_up(data):
    summed = 0

    for market in data:
        for product in data[market]:
            summed += data[market][product]["Menge"] \
                * data[market][product]["Preis"]
            
    return summed

files = glob.glob("Blatt 12/kunde_*")
# print(files)

markets = {}
# markets["Supermarkt 1"] # => Error

for file in files:
    with open(file, 'r') as f:
        entries = json.load(f)
        # print(f"Kunde {file[15:]}: {sum_up(entries):.2f}€")

        # 1.2
        for market in entries:
            if market not in markets:
                markets[market] = {}

            for product in entries[market]:
                if product not in markets[market]:
                    markets[market][product] = 0
                markets[market][product] += entries[market][product]["Menge"]