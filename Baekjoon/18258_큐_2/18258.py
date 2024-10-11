import sys
from collections import deque

input = sys.stdin.readline

def solution(N, commands):
    queue = deque()
    answer = []

    for command in commands:
        if command.startswith('pu'):
            queue.append(command.split()[1])
        elif command.startswith('po'):
            answer.append(queue.popleft() if queue else -1)
        elif command.startswith('s'):
            answer.append(len(queue))
        elif command.startswith('e'):
            answer.append(0 if queue else 1)
        elif command.startswith('f'):
            answer.append(queue[0] if queue else -1)
        else:
            answer.append(queue[-1] if queue else -1)
    
    return answer


if __name__ == '__main__':
    N = int(input().rstrip())
    commands = [input().rstrip() for _ in range(N)]

    answer = solution(N, commands)
    print(*answer, sep='\n')

