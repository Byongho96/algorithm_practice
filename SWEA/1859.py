T = int(input())

for t in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    profit = 0

    while price:
        mx = price[0]
        mxIdx = 0
        for i in range(len(price)):
            if mx < price[i]:
                mx = price[i]
                mxIdx = i
        profit += mx * mxIdx - sum(price[:mxIdx])
        del price[:mxIdx+1]

    print(f'#{t} {profit}')