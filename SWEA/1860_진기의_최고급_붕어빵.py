import sys
sys.stdin= open('input.txt', 'r', encoding='UTF-8')

T = int(input())

for t in range(1, T+1):

    N, M, K = map(int,input().split())
    people = list(map(int,input().split()))
    people.sort()

    result = 'Possible'
    for i, time in enumerate(people):
        bun = time // M * K - i
        if bun <= 0:
            result = 'Impossible'
            break

    print(f'#{t} {result}')

