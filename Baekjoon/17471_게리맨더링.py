from collections import deque
import sys
input = sys.stdin.readline

def is_valid_bfs(arr):
    q = deque()
    visited2 = [0] * (N + 1)

    q.append(arr[0])
    visited2[arr[0]] = 1
    people_area = 0
    cnt = 1
    while q:
        v = q.popleft()
        people_area += people[v]    # bfs 돌리는김에 사람 수 계산까지!!
        for w in adjLst[v]:
            if (w in arr) and not visited2[w]:
                q.append(w)
                visited2[w] = 1
                cnt += 1

    if cnt == len(arr):
        return people_area
    return 0

def backtraking_comb(n, idx):
    global mn
    if n == num_comb:
        area1 = []
        area2 = []
        for i in range(1, N+1):
            if visited[i]:
                area1.append(i)
            else:
                area2.append(i)
        x, y = is_valid_bfs(area1), is_valid_bfs(area2)
        if x and y:
            mn = min(mn, abs(x-y))
    else:
        for i in range(idx + 1, N + 1):
            if not visited[i]:
                visited[i] = 1
                backtraking_comb(n + 1, i)
                visited[i] = 0
        return

N = int(input())
people = [0] + list(map(int, input().rstrip().split()))
adjLst = [[] for _ in range(N+1)]
for i in range(1, N+1):
    adjLst[i].extend(list(map(int, input().rstrip().split()))[1:])

P = sum(people)
mn = P
for num_comb in range(1, N//2 + 1):
    visited = [0] * (N + 1)
    backtraking_comb(0, 0)
    if mn == 0:
        break

if mn == P:
    print(-1)
else:
    print(mn)