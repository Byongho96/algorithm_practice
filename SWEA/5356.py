from itertools import zip_longest

T = int(input())

for t in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    arr = list(zip_longest(*arr, fillvalue='')) #  세로로 묶으면서, 데이터가 없는 곳은 ''을 대입

    result = ''
    for lst in arr:
        result += ''.join(lst)
    print(f'#{t} {result}')