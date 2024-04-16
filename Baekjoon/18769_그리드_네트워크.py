import sys
from typing import List, Tuple

input = sys.stdin.readline

# Baekjoon 18769 그리드 네트워크

def find_set(par: List[int], x:int) -> int:
  while x != par[x]:
      x = par[x]
  return x

def union_by_rank(par: List[int], rank: List[int], x:int, y:int) -> None:
    x_rank = rank[x]
    y_rank = rank[y]

    if x_rank == y_rank:
        par[y] = x
        rank[x] += 1
    elif rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y

def solution(R, C, edges: List[Tuple[int]]) -> int:
    N = R * C
    par = [node for node in range(N)] 
    rank = [0] * N                

    edges.sort(key=lambda x: x[0])

    mst = 0   
    weight = 0 

    for w, n1, n2 in edges:
        N1 = find_set(par, n1)
        N2 = find_set(par, n2)
        if N1 == N2:
            continue  
        union_by_rank(par, rank, N1, N2)  # par, rank모두 참조형 타입으로 넘겨줌
        weight += w
        mst += 1
        if mst == N:  
            break

    return weight

if __name__ =="__main__":
    for _ in range(int(input())):
        R, C = map(int, input().split())
        
        # Get edges [(weight, start, end)]
        edges = []

        # Get edge info left/right
        for i in range(R):
            for j, w in enumerate(map(int, input().split())):
                edges.append((w, i * C + j, i * C + j + 1))

        # Get endge info up/down
        for i in range(R - 1):
            for j, w in enumerate(map(int, input().split())):
                edges.append((w, i * C + j, (i + 1) * C + j ))

        answer = solution(R, C, edges)
        print(answer)