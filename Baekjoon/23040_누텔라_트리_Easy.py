from typing import List, Tuple
from collections import defaultdict
import sys

input = sys.stdin.readline

def solution(N: int, adjLst: Tuple[List[int]], colors: str) -> int:
    start = colors.find('B')
    if start < 0:
        return  0
    
    # DFS
    visited = [False] * (N + 1)
    red_group = defaultdict(set)

    stack = [(start, None)]
    visited[start] = True

    while stack:
        cur, red_root = stack.pop()

        if colors[cur] == 'R':
            red_group[red_root].add(cur)
        else:
            red_root = None

        # 깊이 우선 탐색
        for adj in adjLst[cur]:

            if visited[adj]:
                continue

            visited[adj] = True

            stack.append((adj, red_root if red_root or colors[adj] != 'R' else adj))


    # memoize
    memo = [0] * (N + 1) 
    for red_root in red_group:
        num_red = len(red_group[red_root])
        for red in red_group[red_root]:
            memo[red] = num_red

    # get answer
    answer = 0
    for idx in range(1, N + 1):
        if colors[idx] != 'B':
            continue
        for adj in adjLst[idx]:
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

    answer = solution(N, adjLst, colors)
    print(answer)