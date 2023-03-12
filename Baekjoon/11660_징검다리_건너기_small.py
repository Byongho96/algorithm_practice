N, K = map(int, input().split())
stones = list(map(int, input().split()))

P = [0] * N
P[0] = 1
for i in range(1, N):
    for j in range(i-1, max(0, i-K)-1, -1): # 가까운 것부터 검사해서 break문의 확률을 높임
        if P[j] and (i - j) * (1 + abs(stones[i] - stones[j])) <= K:
            P[i] = 1
            break

if P[-1]:
    print('YES')
else:
    print('NO')
