from collections import deque
import sys
input = sys.stdin.readline

if __name__ =="__main__":
    N = int(input())
    buffer = deque()

    while True:
        packet = int(input())
        if packet == -1:
            break
        if packet == 0:
            buffer.popleft()
        elif len(buffer) < N:
            buffer.append(packet)

    print(*buffer)