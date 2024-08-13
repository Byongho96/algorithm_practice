import sys
from collections import deque
input = sys.stdin.readline

def solution(N, S, positions, fuels):
    cur = S - 1

    left, right = cur, cur
    mx, mn = positions[cur] + fuels[cur], positions[cur] - fuels[cur]

    while True:
        is_updated = False

        # 왼쪽 탐색 
        if left > 0 and mn <= positions[left - 1]:
            left -= 1
            mx = max(mx, positions[left] + fuels[left])
            mn = min(mn, positions[left] - fuels[left])
            is_updated = True

        # 오른쪽 탐색
        if right < N - 1 and mx >= positions[right + 1]:
            right += 1
            mx = max(mx, positions[right] + fuels[right])
            mn = min(mn, positions[right] - fuels[right])
            is_updated = True

        if not is_updated:
      
            break

    return range(left + 1, right + 2)
    

if __name__ == "__main__":
    N, S = map(int, input().split())
    positions = list(map(int, input().split()))
    fuels = list(map(int, input().split()))

    answer = solution(N, S, positions, fuels)
    print(*answer)