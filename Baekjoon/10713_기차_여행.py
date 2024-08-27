import sys
from typing import Tuple
input = sys.stdin.readline

def solution(N:int, M:int, cities:Tuple[int], costs) -> int:
    counts = [0] * (N + 1)

    # 누적합으로 처리하기 위한 마킹
    for station in range(1, M):
        cur = cities[station] - 1
        prev = cities[station - 1] - 1
        factor = 1 if prev < cur else -1

        counts[prev] += factor
        counts[cur] -= factor

    # 누적합으로 처리
    answer = 0
    cumulative = 0 
    for i in range(N - 1):
        cumulative += counts[i]
        answer += min(cumulative * costs[i][0], costs[i][2] + costs[i][1] * cumulative)

    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    cities = tuple(map(int, input().split()))

    # 티켓 비용, 카드 패스 비용, 카드 구매  비용
    costs = tuple(tuple(map(int, input().split())) for _ in range(N - 1))
    answer = solution(N, M, cities, costs)
    print(answer)