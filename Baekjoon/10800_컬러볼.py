import sys
from typing import List, Tuple

input = sys.stdin.readline

def solution(N:int, balls: List[Tuple[int]]) -> List[int]:
    # total cumulative sum
    total = 0
    total_by_color = [0] * (N + 1)

    # buffer cumulative sum
    # [sum of buffer, ball size]
    buffer_size_total = [0, 0] 
    buffer_size_by_color = [[0, 0] for _ in range(N + 1)]
    
    # sort by size
    balls.sort(key=lambda x: x[1])

    answer = [0] * N
    for i in range(N):
        color, size, idx = balls[i]

        # transfer the buffer
        if buffer_size_total[1] != size:
            total += buffer_size_total[0]
            buffer_size_total[0] = 0

        if buffer_size_by_color[color][1] != size:
            total_by_color[color] += buffer_size_by_color[color][0]
            buffer_size_by_color[color][0] = 0

        # calculate the sum of catchable balls size
        answer[idx] = total - total_by_color[color]

        # record the data into the buffer
        buffer_size_total[0] += size
        buffer_size_total[1] = size
        buffer_size_by_color[color][0] += size
        buffer_size_by_color[color][1] = size

    return answer

if __name__ == "__main__":
    N = int(input())
    balls = [list(map(int, input().split())) + [i] for i in range(N)]

    answer = solution(N, balls)
    print(*answer, sep="\n")