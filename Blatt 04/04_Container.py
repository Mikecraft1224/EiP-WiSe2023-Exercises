for i in range(5):
    containers = []

    # f = open(f"container{i}.txt")
    # ...
    # f.close()

    with open(f"Blatt 04/container{i}.txt") as f:
        for line in f.readlines():
            if line.strip() != "":
                containers.append(line.strip().split(" "))
                # "5 1" => ["5", "1"]

    higher = [c[0] for c in containers]
    lower = [c[1] for c in containers]
    # list(set(...)) => remove duplicates
    candidates = list(set([c for c in higher if c not in lower]))

    if len(candidates) == 1:
        print(f"Heaviest container is {candidates[0]}")
    else:
        print(f"Cannot determine heaviest container, candidates are {candidates}")