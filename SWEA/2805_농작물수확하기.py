import sys
sys.stdin = open('input.txt','r',encoding='UTF-8')

def my_sum(arr):
    sum = 0
    for ele in arr:
        sum += ele
    return sum

def my_abs(i):
    return (i if i >=0 else -i)

for T in range(1, int(input())+1):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]

    hrvst = 0
    n = N//2
    for i, row in enumerate(farm):
        i = n - abs(n-i)
        hrvst += my_sum(row[n-i:n+i+1])
        ''' Idea
        0 row:      N//2
        1 row:      N//2-1 ~ N//2+1
        ~
        N//2 row:   N//2-(N//2) ~ N//2 +(N//2)
        ~
        N-2 row:    N//2-1 ~ N//2+1
        N-1 row:    N//2
        '''
        # i row: N//2-i ~ N//2+i
        # i: 0 -> N//2 -> 0
        # i = N//2 - abs(N//2-i)
    print(f'#{T} {hrvst}')

