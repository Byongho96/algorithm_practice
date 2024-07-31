from typing import List, Tuple
import sys
input = sys.stdin.readline

# DFS
def find_the_farthest(N:int, start: int, adjLst: List[List[int]]) -> Tuple[int, int]:
    distance = [0] * (N + 1)

    stack = [start]
    distance[start] = 1

    while stack:
        cur = stack.pop()

        for adj in adjLst[cur]:
            if distance[adj]:
                continue

            distance[adj] = distance[cur] + 1
            stack.append(adj)

    mx = max(distance)
    farthest = distance.index(mx)

    return farthest, mx - 1

def solution(N: int, adjLst: List[int]) -> int:
    start, _ = find_the_farthest(N, 1, adjLst)
    _, distance = find_the_farthest(N, start, adjLst)

    distance = (distance + 1) // 2

    return distance

if __name__ == "__main__":
    N = int(input())

    adjLst = tuple([] for _ in range(N + 1))
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adjLst[u].append(v)
        adjLst[v].append(u)
    
    answer = solution(N, adjLst)
    print(answer)