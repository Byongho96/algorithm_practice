import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def dfs(i, j):
    # visited = [[0] * N for _ in range(N)] # 어차피 되돌아 올 일 없음
    stk = []

    rooms = 1   # 방문한 방의 갯수
    while True:
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:    # 마지막 조건 때문에 visited 필요없음
                stk.append((i, j))
                i, j = ni, nj
                rooms += 1  # 방문한 방 수 업데이트
                break
        else:               # 더 이상 움직 일 수 없으면
            return rooms        # 방문한 방의 갯수 리턴

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    start = 0
    for i in range(N):
        for j in range(N):
            rooms = dfs(i, j)
            if rooms > mx:          # 방문한 방의 갯수가 현재 최댓값 보다 많으면
                mx = rooms
                start = arr[i][j]
            elif rooms == mx:       # 방문한 방의 갯수가 현재 최댓갑과 같으면
                start = min(start, arr[i][j])

    print(f'#{tc} {start} {mx}')