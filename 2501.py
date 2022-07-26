import sys

N, K = map(int, sys.stdin.readline().split())
com_div = [1]

for i in range(2, N):
    if not N % i:
        com_div.append(i)
com_div.append(N)

if len(com_div) < K:
    print(0)
else:
    print(com_div[K - 1])


''' 최단시간 문제 참조
import sys

N, K = map(int, sys.stdin.readline().split())

com_div = [i for i in range(1, N+2) if N % i == 0]

print(0 if len(com_div) < K else com_div[K-1])
'''