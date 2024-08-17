import sys
input = sys.stdin.readline

def find_parent(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union_by_rank(parent, rank, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a == b:
        return False

    if rank[a] < rank[b]:
        a, b = b, a

    parent[b] = a

    if rank[a] == rank[b]:
        rank[a] += 1

    return True

def solution(N, M, t, edges):
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    cnt = 0
    answer = (N - 2) * (N - 1) // 2 * t
    for a, b, c in edges:
        if not union_by_rank(parent, rank, a, b):
            continue
        cnt += 1
        answer += c
        if cnt == N - 1:
            break

    return answer


if __name__ == "__main__":
    N, M, t = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    answer = solution(N, M, t, edges)
    print(answer)