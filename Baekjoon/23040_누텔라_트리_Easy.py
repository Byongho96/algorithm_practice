
from typing import List, Tuple
import sys

input = sys.stdin.readline

def solution(N:int, adjLst:Tuple[List[int]], clrs:str) -> int:
    memo = {}
    answer = 0
    colors = 'G' + clrs

    for start in range(1, len(colors)):
        color = colors[start]
        if color != 'B':
            continue

        visited = [False] * (N + 1)
        stack = []
        cur = start

        while True:
            for adj in adjLst[cur]:
                if visited[adj] or colors[adj] != 'R' or (cur, adj) in memo:
                    continue
                stack.append(cur)
                cur = adj
                visited[cur] = True
                break

            else:
                if stack:
                    sm = 1
                    for adj in adjLst[cur]:
                        sm += memo.get((cur, adj), 0)
                    memo[(stack[-1], cur)] = sm
                    cur = stack.pop()
                else:
                    for adj in adjLst[cur]:
                        answer += memo.get((cur, adj), 0)
                    break

    return answer


if __name__ == "__main__":
    N = int(input())

    adjLst = tuple([] for _ in range(N + 1)) # adjacent list
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adjLst[u].append(v)
        adjLst[v].append(u)

    colors = input().rstrip()

    answer = solution(N, adjLst, colors)
    print(answer)