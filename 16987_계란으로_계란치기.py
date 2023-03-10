def backtracking(cur, N):
    global max_broken

    # 1. 종료 조건
    if cur == N:
        max_broken = max(max_broken, sum(broken))
        return

    # 2. 가지 치기
    if sum(broken) == N:
        max_broken = N
        return
    
    if max_broken == N:
        return
    
    # 3. 후보군 출력
    if broken[cur] or sum(broken) == N-1:
        backtracking(cur + 1, N)
        return

    for tar in range(N):
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
        # 계란 복구
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
