T = int(input())

for t in range(1, T+1):
    N = int(input())
    result = [0]* 8

    for i, m in enumerate((50000, 10000, 5000, 1000, 500, 100, 50, 10)):
        while N >= m:
            N -= m
            result[i] += 1
        
    print(f'#{t}')
    print(*result)