if __name__ == "__main__":
    address = input().split(":")

    # rule 2
    if "" in address:
        idx = address.index("")
        while "" in address:
            address.remove("")
        address = address[:idx] + ["0000"] * (8 - len(address)) + address[idx:]

    # rule 1
    for i in range(8):
        L = len(address[i])
        if L < 4:
            address[i] = "0" * (4 - L) + address[i]

    print(*address, sep=":")
