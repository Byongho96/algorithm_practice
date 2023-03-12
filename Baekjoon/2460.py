p = 0
max = 0

for _ in range(10):
    off, on = map(int, input().split())
    p = p - off + on
    if p > max:
        max = p

print(max)