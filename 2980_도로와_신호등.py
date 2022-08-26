N, L = map(int, input().split())

wait_time = 0                   # 신호등을 기다린 모든 시간을 더하는 변수

for _ in range(N):
    D, R, G = map(int, input().split())

    time = D + wait_time            # 해당 신호등에 도착하기까지 걸린시간 = 신호등까지 거리 + 이전에 신호등을 기다린 시간

    is_red = R - time % (R + G)     # is_red > 0이면, 현재 파란불까지 남은 시간을 가리킴
    if is_red < 0:                  # 따라서 is_red < 0 일 때는, 기다릴 필요 없이 통과
        wait_time += 0
    else:                           # is_red > 0일 대는, wait_time 업데이트
        wait_time += is_red

ans = L + wait_time             # 최종 도착 시간 = 도로 거리 + 신호등을 기다린 시간
print(ans)

