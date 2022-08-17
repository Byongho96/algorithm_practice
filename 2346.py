from collections import deque

N = int(input())
balloons = deque(enumerate(map(int, input().split())))
ptr = 0

for _ in range(N):
    nxt = balloons.popleft()
    print(nxt[0]+1, end =' ')
    if nxt[1] > 0:
        balloons.rotate(-nxt[1]+1)
    else:
        balloons.rotate(-nxt[1])