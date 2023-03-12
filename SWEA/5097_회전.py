import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    print(f'#{t} {nums[M % N]}')