import sys
input = sys.stdin.readline

def solution(N, waiting_list):
    entered = [False] * N
    waiting_list.sort(key=lambda x: (x[1], x[0]))   # 도착 시간, 예약시간 순으로 정렬

    immediately_enter_map = {}  # 즉시 입장하는 손님들, 도착 시간이 예약 시간보다 빠른 경우
    for i in range(N):
        if waiting_list[i][1] < waiting_list[i][0] + 1: 
            immediately_enter_map[waiting_list[i][0]] = i

    answer = 0

    idx = 0 # 대기 손님 인덱스
    cur_time = waiting_list[0][1]
    while idx < N:
        # 예약 손님이 있을 경우, 먼저 입장
        reserved_idx = immediately_enter_map.get(cur_time)
        if reserved_idx and not entered[reserved_idx]:
            entered[reserved_idx] = True
            answer = max(answer, cur_time - waiting_list[reserved_idx][1])
            cur_time += 1
            continue

        if entered[idx]:
            idx += 1
            continue

        # 가장 앞의 손님 입장
        if (waiting_list[idx][1] < cur_time + 1):
            entered[idx] = True
            answer = max(answer, cur_time - waiting_list[idx][1])
            idx += 1
            cur_time += 1
            continue

        cur_time = waiting_list[idx][1] # 다음 대기 손님 시간

    return answer

if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = solution(N, arr)
    print(answer)