import sys
input = sys.stdin.readline

def solution(N, M, K, board):
    mid = K * K // 2
    white_start = [[0] * (M + 1) for _ in range(N + 1)]

    # 누적합 생성
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if (i + j) % 2:
                white_start[i][j] = white_start[i - 1][j] + white_start[i][j - 1] - white_start[i - 1][j - 1] + board[i][j]
            else:
                white_start[i][j] = white_start[i - 1][j] + white_start[i][j - 1] - white_start[i - 1][j - 1] + 1 - board[i][j]  

    # 계산
    answer = N * M
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            white = white_start[i + K - 1][j + K - 1] - white_start[i - 1][j + K - 1] - white_start[i + K - 1][j - 1] + white_start[i - 1][j - 1]
            answer = min(answer, K * K - white if white > mid else white)

            if not answer:
                return 0

    return answer

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    board = [[0] * (M + 1)] + [[0] + list(map(lambda x: 0 if x == 'B' else 1, input().rstrip())) for _ in range(N)]

    answer = solution(N, M, K, board)
    print(answer)