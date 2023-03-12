import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

from collections import deque

def calculate_dis_R(G, P, visited):
    left = G
    right = G

    cnt = 0
    dis = 0

    if not visited[G]:
        visited[G] = 1
        cnt = 1
        dis = 1

    while cnt != P:
        if right < N:
            right += 1
            if not visited[right]:
                visited[right] = 1
                cnt += 1
                dis += (right - G) + 1
                if cnt == P:
                    break
        if left > 1:
            left -= 1
            if not visited[left]:
                visited[left] = 1
                cnt += 1
                dis += (G - left) + 1
    return dis

def calculate_dis_L(G, P, visited):
    left = G
    right = G

    cnt = 0
    dis = 0

    if not visited[G]:
        visited[G] = 1
        cnt = 1
        dis = 1

    while cnt != P:
        if left > 1:
            left -= 1
            if not visited[left]:
                visited[left] = 1
                cnt += 1
                dis += (G - left) + 1
                if cnt == P:
                    break
        if right < N:
            right += 1
            if not visited[right]:
                visited[right] = 1
                cnt += 1
                dis += (right - G) + 1
    return dis

def dfs_recursive(n, visited):
    global mn
    if n == 3:
        tmp = sum(dis)
        if tmp < mn:
            mn = tmp
    else:
        tmp_visited = visited
        dis[n] = calculate_dis_L(G[perm[n]], P[perm[n]], tmp_visited)
        dfs_recursive(n + 1, tmp_visited)
        tmp_visited2 = visited
        dis[n] = calculate_dis_R(G[perm[n]], P[perm[n]], tmp_visited2)
        dfs_recursive(n + 1, tmp_visited2)

T = int(input())
for t in range(1, T+1):

    N = int(input())
    G = [0] * 3
    P = [0] * 3
    G[0], P[0] = map(int, input().split())
    G[1], P[1] = map(int, input().split())
    G[2], P[2] = map(int, input().split())

    mn = (P[0] + P[1] + P[2]) * N

    for perm in ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 1, 0), (2, 0, 1)):
        visited = [0] * (N + 1)
        dis = [0] * 3
        dfs_recursive(0, visited)

    print(f'#{t} {mn}')