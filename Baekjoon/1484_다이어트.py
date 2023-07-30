if __name__ == '__main__':

    print([[0 for _ in range(2+1)] for _ in range(2+1)])
    G = int(input())

    prev, cur = 1, 1

    is_available = False
    while True:
        diff = cur ** 2 - prev ** 2
        if diff > G:
            if cur == prev + 1:
                break
            prev += 1
            continue
        if diff == G:
            is_available = True
            print(cur)
        cur += 1
    
    if not is_available:
        print(-1)