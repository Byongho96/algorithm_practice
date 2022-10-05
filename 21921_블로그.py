import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visited = list(map(int, input().split()))

cnt = 1
mx = sum(visited[:X])
people = mx
for i in range(N - X):
    people = people - visited[i] + visited[i+X]
    if people > mx:
        mx = people
        cnt = 1
    elif people == mx:
        cnt += 1

if mx:
    print(mx)
    print(cnt)
else:
    print('SAD')

