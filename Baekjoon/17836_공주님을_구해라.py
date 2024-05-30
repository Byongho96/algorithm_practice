import sys
import heapq

input = sys.stdin.readline

INF = 100 * 100 + 1
DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))

def a_star(N, M, T, arr):
    distance = [[[INF, INF] for _ in range(M)] for _ in range(N)]

    distance[0][0][0] = 0
    heap = [(N - 1 + M - 1, 0, 0, 0, 0)] # estimated, time, i, j, isGram

    while heap:
        h, t, i, j, isGram = heapq.heappop(heap)

        # pruning
        if t > distance[i][j][isGram]:
            continue

        # early end condition
        if t > T:
            return False

        # end condition
        if i == N - 1 and j == M - 1:
            return t
        
        # visit the node
        if arr[i][j] == 2:
            isGram = True

        # traverse adjacent nodes
        for di, dj in DIRECTION:
            ni = i + di
            nj = j + dj
            nt = t + 1
            nh = nt + (N - 1 - ni) + (M - 1 - nj)
            if -1 < ni < N and -1 < nj < M and (arr[ni][nj] != 1 or isGram) and distance[ni][nj][isGram] > nt:
                distance[ni][nj][isGram] = nt
                heapq.heappush(heap, (nh, nt, ni, nj, isGram))

    return False

if __name__ == '__main__':
    N, M, T = map(int, input().split())
    arr =  [list(map(int, input().split())) for _ in range(N)]

    answer = a_star(N, M, T, arr)

    print (answer if answer else 'Fail')



