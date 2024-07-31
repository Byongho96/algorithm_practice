from typing import List, Tuple
from collections import defaultdict
import sys

input = sys.stdin.readline

# DFS
def memoize(N: int, adjLst: Tuple[List[int]], colors: str, start: int) -> List[int]:
    memo = [-1] * (N + 1) 
    red_group = defaultdict(set)
    stack = []

    cur, black = start, start

    while True:
        # 노드 방문
        memo[cur] = 0

        # 깊이 우선 탐색
        for adj in adjLst[cur]:

            if memo[adj] > -1:
                continue

            stack.append((cur, black))

            cur = adj
            if colors[cur] == 'B':
                black = cur
            else:
                red_group[black].add(cur)
            break

        else:
            if stack:
                cur, black = stack.pop()
                if cur == black: # colors[cur] == 'B'
                    num_red = len(red_group[cur])
                    for red in red_group[cur]:
                        memo[red] = num_red
                    del red_group[cur]

            else:
                break

    return memo


def solution(N:int, adjLst:Tuple[List[int]], colors:str) -> int:
    black = colors.find('B')
    if black < 0:
        return  0
    
    memo = memoize(N, adjLst, colors, black)

    answer = 0
    for start in range(1, len(colors)):
        if colors[start] != 'B':
            continue

        for adj in adjLst[start]:
            answer += memo[adj]

    return answer

def find(parent, u):
    while parent[u] != u:
        u = parent[u]
    return u

def union_by_rank(parent, rank, size, u, v):
    u = find(parent, u)
    v = find(parent, v)

    if u == v:
        return

    if rank[u] > rank[v]:
        u, v = v, u

    parent[u] = v
    size[v] += size[u]
    if rank[u] == rank[v]:
        rank[v] += 1

def solution2(N:int, adjLst:Tuple[List[int]], colors:str) -> int:
    # divide red and black
    red_set = set()
    black_set = set()
    for i in range(1, N + 1):
        if colors[i] == 'R':
            red_set.add(i)
        else:
            black_set.add(i)

    # connect red
    parent = [i for i in range(N + 1)]
    size = [1] * (N + 1)
    rank = [0] * (N + 1)

    for red in red_set:
        for adj in adjLst[red]:
            if adj in red_set:
                union_by_rank(parent, rank, size, red, adj)

    # calculate answer
    answer = 0  
    for black in black_set:
        for adj in adjLst[black]:
            if adj in red_set:
                answer += size[find(parent, adj)]
    
    return answer

if __name__ == "__main__":
    N = int(input())

    adjLst = tuple([] for _ in range(N + 1)) # adjacent list
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adjLst[u].append(v)
        adjLst[v].append(u)

    colors = 'G' + input().rstrip()

    answer = solution2(N, adjLst, colors)
    print(answer)