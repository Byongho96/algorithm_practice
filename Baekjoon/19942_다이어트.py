import sys
input = sys.stdin.readline

mn = 500 * 15 + 1
bits = 0

def backtracking(N, required, consumed, info, bit, idx, cost):
    global mn, bits

    
    if cost > mn - 1:
        return 

    for i in range(4):
        if required[i] > consumed[i]:
            break
    else:
        mn = cost
        bits = bit
        return
    
    if idx == N:
        return

    # 구매
    new_consumed = [consumed[i] + info[idx][i] for i in range(4)] 
    backtracking(N, required, new_consumed, info, bit | 1 << idx, idx + 1, cost + info[idx][4])

    # 구매하지 않음
    backtracking(N, required, consumed, info, bit, idx + 1, cost)


def solution(N, requried, info):
    global mn, bits

    mn = 500 * N + 1
    bits = 0

    backtracking(N, required, [0] * 4, info, 0, 0, 0)

    if not bits:
        return -1, []

    items = []
    for i in range(N):
        if bits >> i & 1:
            items.append(i + 1)

    return mn, items


if __name__ == "__main__":
    N = int(input())
    required = list(map(int, input().split()))
    info = [list(map(int, input().split())) for _ in range(N)]

    cost, items = solution(N, required, info)

    if cost == -1:
        print(-1)
    else:
        print(cost, *items, sep='\n')