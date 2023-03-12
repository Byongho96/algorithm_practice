def find_7dwarfs():

    dwarfs = []

    for _ in range(9):
        dwarfs.append(int(input()))

    sum_dwarfs = sum(dwarfs)

    for i in range(8):
        for j in range(i+1, 9):
            if sum_dwarfs - dwarfs[i] - dwarfs[j] == 100:
                del dwarfs[j]
                del dwarfs[i]
                return sorted(dwarfs)

for dwarf in find_7dwarfs():
    print(dwarf)
