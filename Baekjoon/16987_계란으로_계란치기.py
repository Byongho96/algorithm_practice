def backtracking(cur, N):
    global max_broken

    # 1. 종료 조건
    if cur == N:
        max_broken = max(max_broken, sum(broken))
        return

    # 2. 가지 치기
    if max_broken == N:     # 이미 다른 경우에서 최대 값이 나온 경우 -> 종료
        return
    
    if sum(broken) == N:    # 최대 값을 도달한 경우 -> max_broken 업데이트 후 종료
        max_broken = N
        return
    
    # 3. 후보군 출력
    if broken[cur] or sum(broken) == N-1:   # 손에 든 달걀이 깨졌거나, 다른 달걀들이 모두 깨졌으면 -> 다음으로 넘어감
        backtracking(cur + 1, N)
        return

    for tar in range(N):    # 깨지지 않은 다른 달걀이 있으면 깨기
        if broken[tar]:
            continue
        if tar == cur:
            continue
        # 계란 깨기
        durability[tar] -= weight[cur]
        durability[cur] -= weight[tar]
        if durability[tar] <= 0:
            broken[tar] = 1
        if durability[cur] <= 0:
            broken[cur] = 1
        backtracking(cur + 1, N)
        # 다음 반복문을 위해 계란 복구
        durability[tar] += weight[cur]
        durability[cur] += weight[tar]
        if durability[tar] > 0:
            broken[tar] = 0
        if durability[cur] > 0:
            broken[cur] = 0

    return 

N = int(input())

durability = [0] * N
weight = [0] * N
broken = [0] * N
for tar in range(N):
    durability[tar], weight[tar] = map(int, input().split())

max_broken = 0
backtracking(0, N)

print(max_broken)
