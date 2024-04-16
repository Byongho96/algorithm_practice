def solution(N, M, arr):
    if check(): # 모든 좌표를 탐색한 경우
        answer = min(answer, cnt) # answer를 최솟값으로 갱신
    if cnt < answer: # 현재까지 탐색한 경로의 수가 answer보다 작을 경우만 탐색
        for i in range(4): # 4방향 탐색
            tmp = [] # 지나온 좌표를 담을 배열
            ax = x
            ay = y
            while True:
                ax += d[i][0]
                ay += d[i][1]
                if 0 <= ax < N and 0 <= ay < M and board[ax][ay] == ".": # 구슬을 놓을 수 있는 공간이라면 다음 좌표 탐색
                    tmp.append([ax, ay])
                    board[ax][ay] = "*"
                else: # 구슬을 놓을 수 없다면 탐색 종료
                    break
            if tmp: bt(ax-d[i][0], ay-d[i][1], cnt + 1) # tmp가 비어있지 않다는 것은 탐색을 진행했다는 것이므로 다음 경로의 탐색도 진행하여야 함.
            for a,b in tmp: # 현재까지 지나온 좌표를 다시 "." 로 초기화
                board[a][b] = "."
        board[x][y] = "." # 시작좌표를 "."로 초기화


if __name__== "__main__":
    i = 0
    while True:
        try:
            i += 1
            N, M = map(int, input().split())
            arr = [input().split() for _ in range(N)]

            answer = solution(N, M, arr)
            print(f'Case {i}: {answer}')

        except:
            break