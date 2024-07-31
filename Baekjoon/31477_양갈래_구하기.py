from typing import List, Tuple, Dict
import sys

sys.setrecursionlimit(10 ** 6)  

input = sys.stdin.readline


def backtracking(par:int, cur:int, adjLst: Tuple[Dict[int, int]]) -> int:
    mn = adjLst[par][cur]

    sm = 0
    for adj in adjLst[cur]:
        if adj == par:
            continue
        sm += backtracking(cur, adj, adjLst)

    return min(mn, sm) if sm else mn

def solution(N: int, adjLst: Tuple[Dict[int, int]]) -> int:
    answer = 0
    for adj in adjLst[1]:
        answer += backtracking(1, adj, adjLst)

    return answer


if __name__ == "__main__":
    N = int(input())

    adjLst = tuple({} for _ in range(N + 1)) # adjacent list
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        adjLst[u][v] = w
        adjLst[v][u] = w

    answer = solution(N, adjLst)
    print(answer)