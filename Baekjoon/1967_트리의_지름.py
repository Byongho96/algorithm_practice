from collections import defaultdict

import sys
input = sys.stdin.readline

def find_the_farthest(N, adjLst, start):
    stack = []
    visited = [False] * (N + 1)
    
    # set the start point
    stack.append((start, 0))
    visited[start] = True

    # find the farthest with dfs
    the_farthest = 0
    the_distance = 0
    while stack:
        cur, dis = stack.pop()

        if dis > the_distance:
            the_distance = dis
            the_farthest = cur
        
        for adj, w in adjLst[cur]:
            if visited[adj]:
                continue
            new_dis = dis + w
            stack.append((adj, new_dis))
            visited[adj] = True

    return the_farthest, the_distance


if __name__ == '__main__':
    N = int(input())

    # adjacent node lists dictionary
    adjLst = defaultdict(list)
    for _ in range(N - 1):
        i, j, w = map(int, input().split())
        adjLst[i].append((j, w))
        adjLst[j].append((i, w))

    # find the farthest leaf node
    one, _ = find_the_farthest(N, adjLst, 1)

    # find the other farthest node
    the_other, diameter = find_the_farthest(N, adjLst, one)

    print(diameter)