import sys
# import math

N = int(sys.stdin.readline())

x = (N // 7) + 4 if N % 7 else (N // 7) + 3

#x = math.ceil(N / 7 + 3) # N = (x + (x-6)) * 7 / 2 

if N < 28:
    for i in range(1, 7):
        M = (1 + i) * i // 2
        if N <= M:
            x = i
            break

print(x)

'''최단시간 코드 참고
import sys
N = int(sys.stdin.readline())

if N <= 28:
    for i in range(1, 8):
        if N <= (1 + i) * i // 2:
            print(i)
            break
else:
    print((N+6) // 7 + 3)
'''