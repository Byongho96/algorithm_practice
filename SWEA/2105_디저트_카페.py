import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

d1 = [-1, 1, 1, -1]
d2 = [1, 1, -1., -1]

def brute_force(n, i, j, sum):

    global result
    if n == 4:
        result = max(result, sum)
        return

    if n == 0 or n == 1:            # 0, 1단계에서는 하나씩 증가하면서 재귀여부 판단
        di = d1[n]
        dj = d2[n]
        for dist in range(1, N):    # 한칸씩 전진하면서
            ni = int(i + di * dist)
            nj = int(j + dj * dist)
            if 0 <= ni < N and 0 <= nj < N and not eaten[arr[ni][nj]]:  # 가능하면 재귀 호출
                eaten[arr[ni][nj]] = 1                                      # 먹은 디저트 번호 업데이트
                pre_dist[n] = dist                                          # 3, 4단계에서 참고할 거리값
                brute_force(n + 1, ni, nj, sum + dist)                      # 재귀호출
            else:                                                       # 불가능한 지점 만나면
                for d in range(1, dist):                                    # 먹은 디저트 번호 복원
                    ni = int(i + di * d)
                    nj = int(j + dj * d)
                    eaten[arr[ni][nj]] = 0
                break
        return

    if n == 2 or n == 3:            # 2, 3단계에서는 0, 1 단계에서 설정된 거리로 탐색
        di = d1[n]
        dj = d2[n]
        distance = pre_dist[n-2]
        ni, nj, dist = -1, -1, 1
        for dist in range(1, distance+ 1):  # 지정된 거리까지 탐색
            ni = int(i + di * dist)
            nj = int(j + dj * dist)
            if 0 <= ni < N and 0 <= nj < N and not eaten[arr[ni][nj]]:
                eaten[arr[ni][nj]] = 1
            else:                               # 하나라도 아니면, for문 브레이크
                for d in range(1, dist):  # eaten 복원
                    ni = int(i + di * d)
                    nj = int(j + dj * d)
                    eaten[arr[ni][nj]] = 0
                break
        else:                               # 모두 완료된 경우에만 다음 재귀 호출
            brute_force(n + 1, ni, nj, sum + pre_dist[n - 2])
            for d in range(1, dist + 1):        # eaten 복원
                ni = int(i + di * d)
                nj = int(j + dj * d)
                eaten[arr[ni][nj]] = 0
        return



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = -1
    pre_dist = [0, 0]
    for i in range(1, N):
        for j in range(N-1):
            eaten = [0] * 101
            brute_force(0, i, j, 0)

    print(f'#{tc} {result}')