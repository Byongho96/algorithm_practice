n, m, r = map(int, input().split())

items = list(map(int, input().split()))

adjLst = ([] for _ in range(n + 1))

for _ in range(r):
    n1, n2, w = map(int, input().split())
    adjLst[n1].append((w, n2))

