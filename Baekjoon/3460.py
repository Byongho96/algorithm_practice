import sys

T = int(sys.stdin.readline())


for _ in range(T):
    N = int(sys.stdin.readline())
    i = 0
    for s in bin(N).lstrip('0b')[::-1]:
        if s == '1':
            print(i, end = ' ')
        i += 1

'''최단시간
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = f'{int(sys.stdin.readline()):b}'[::-1]
    G = (b for b in range(len(N)) if N[b] == '1')
    print(*G)
'''
