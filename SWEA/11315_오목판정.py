import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def rotate(board):
    arr = [[0]*N for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(N):
            arr[j][N-1 - i] = board[i][j]
    return arr

def check(board, N):
    global result
    # 행열 체크
    for _ in range(2):
        for row in board:
            cnt = 0
            for j in range(1, N):
                if row[j] == 'o' and row[j-1] == 'o':
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 4:
                    result = 'YES'
                    return
        board = list(zip(*board))
    # 대각선 체크
    for _ in range(2):
        i = 0
        for j in range(N - 5 + 1):
            cnt = 0
            for d in range(1, N - j):
                if board[i + d][j + d] == 'o' and board[i + d - 1][j + d - 1] == 'o':
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 4:
                    result = 'YES'
                    return
        j = 0
        for i in range(1, N - 5 + 1):
            cnt = 0
            for d in range(1, N - i):
                if board[i + d][j + d] == 'o' and board[i + d - 1][j + d - 1] == 'o':
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 4:
                    result = 'YES'
                    return
        board = rotate(board)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    result = 'NO'
    check(board, N)
    print(f'#{t} {result}')
