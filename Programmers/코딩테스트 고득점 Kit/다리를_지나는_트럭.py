from collections import deque

def solution(bridge_length, weight, truck_weights):
    N = len(truck_weights)  # 트럭 갯수
    
    stack = []                      # 통과한 트럭 리스트
    waiting = deque(truck_weights)  # 다리 진입 전 트럭 리스트
    bridge = deque()                # 다리 위 트럭 리스트
    bridge_time = deque()           # 다리 위 트럭 리스트 남은 거리
    
    time = 0
    while len(stack) < N:
        if bridge_time and bridge_time[0] == 0: # 다리 위 가장 앞 트럭이 끝에 다다랐을 경우
            stack.append(bridge.popleft())      # 해당 트럭을 통과한 트럭 리스트로 옮김
            bridge_time.popleft()
            
        if waiting and sum(bridge) + waiting[0] <= weight:  # 다리 위에 트럭이 더 올라갈 수 있을 경우
            bridge.append(waiting.popleft())    # 대기 중 트럭 하나가 다리 위로 올라옴
            bridge_time.append(bridge_length)
            
        for i in range(len(bridge_time)):   # 초마다 다리 위 트럭의 위치를 왼쪽으로 옮김
            bridge_time[i] -= 1
            
        time += 1   # 시간 1초 증가
    return time