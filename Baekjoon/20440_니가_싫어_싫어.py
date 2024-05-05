import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(N, time_table):
    mx, cur = 0, 0
    start, end = 0, 0
    is_start = False

    keys = list(time_table.keys())
    keys.sort()
    for time in keys:
        cnt = time_table[time]
        cur += cnt
        if cur > mx:
            mx = cur
            start = time
            is_start = True
        elif cnt < 0 and cur - cnt == mx and is_start:
            end = time
            is_start = False
    return (mx, start, end)

if __name__ == "__main__":
    N = int(input())
    time_table = defaultdict(int)
    for _ in range(N):
        s, e = map(int, input().split())
        time_table[s] += 1
        time_table[e] -= 1

    (mx, start, end) = solution(N, time_table)
    print(mx, f'{start} {end}', sep='\n')
