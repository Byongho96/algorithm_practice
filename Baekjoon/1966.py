from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    pQue = list(map(int, input().split()))
    ptr = -1
    cnt = 0

    for _ in range(N):
        ptr = (ptr + 1) % N
        mx = pQue[ptr]
        mxIdx = ptr
        for j in range(ptr, ptr+N):
            j = j % N
            if mx < pQue[j]:
                ptr = j
                mx = pQue[ptr]
        pQue[ptr] = 0
        cnt += 1
        if ptr == M:
            break
    print(cnt)