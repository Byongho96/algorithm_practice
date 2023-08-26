import sys
input = sys.stdin.readline

# DFS
def distribute_worm(arr, i, j):
    di = (0, 0, 1, -1)
    dj = (1, -1, 0, 0)
    stack = [(i, j)]

    # DFS
    while stack:
        i, j = stack.pop()

        # visit the node
        arr[i][j] = 0
        
        # traverse the adjacent nodes
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if not arr[ni][nj]:
                continue
            stack.append((ni, nj))

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        M, N, K = map(int, input().split())

        # make the arr
        arr = [[0] * (M + 2) for _ in range(N + 2)]
        for _ in range(K):
            j, i = map(int, input().split())
            arr[i + 1][j + 1] = 1

        # count the required num of  worms
        num_worms = 0
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if not arr[i][j]:
                    continue
                num_worms += 1
                distribute_worm(arr, i, j)

        print(num_worms)