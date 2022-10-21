import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
dic = {i: 0 for i in range(1, 100001)}

cnt, i, j = 0, 0, 0
for j in range(N):
    dic[lst[j]] += 1
    if dic[lst[j]] > K:
        while True:
            dic[lst[i]] -= 1
            if lst[i] == lst[j]:
                i += 1
                break
            i += 1
    cnt = max(cnt, j - i + 1)

print(cnt)