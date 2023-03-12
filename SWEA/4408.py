T = int(input())

for t in range(1, T+1):
    N = int(input())    # 돌아가야 하는 학생 수
    corridor = [0] * 200    # 복도리스트. value: 해당칸을 지나는 학생 수
    for _ in range(N):
        start, end = map(lambda x: (int(x) - 1)//2, input().split())    # lambda함수: 호실 -> 대응하는 복도 위치
        if start > end: # 출발위치가 도착위치보다 작도록 조정
            start, end = end, start
        for i in range(start, end+1):
            corridor[i] += 1    # 시작호실 ~ 목표호실까지의 값 +1
    time = max(corridor)    # time은 corridor 리스트의 가장 큰 값
                            # 학생이 최대로 겹치는 이동경로 == 최대 단위시간
    print(f'#{t} {time}')