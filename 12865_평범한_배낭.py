import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weight = [0] * (N + 1)  # DP배열의 행과 인덱스를 맞추기 위해서 0번째 인덱스 추가
value = [0] * (N + 1)   # DP배열의 행과 인덱스를 맞추기 위해서 0번째 인덱스 추가
for i in range(1, N + 1):
    weight[i], value[i] = map(int, input().split())

# [1]. 2차원 DP [228MB, 6956ms]
DP = [[0] * (K + 1) for _ in range(N + 1)]  # 행: 물건의 갯수 (0 ~ N) / 열: 가방의 최대용량(0 ~ K)
for cur_object in range(1, N + 1):          # cur_object: 1부터 N까지 증가
    for limit in range(1, K + 1):               # limit: 가방의 최대용량을 1부터 K까지 증가
        # 메인 아이디어
        if weight[cur_object] <= limit:                     # 현재 물건의 무게가 가방의 최대 용량 이하라면
                                                                # 현재 물건을 안 넣는 경우, 현재 물건의 무게만큼 빼고 현재 물건을 넣은 경우 중 큰 것
            DP[cur_object][limit] = max(DP[cur_object-1][limit], DP[cur_object-1][limit-weight[cur_object]] + value[cur_object])
        else:                                               # 현재 물건의 무게가 가방의 최대 용량 보다 크다면
            DP[cur_object][limit] = DP[cur_object - 1][limit]   # 현재 물건을 넣지 못한다
print(DP[-1][-1])

# [2]. 1차원 DP [34MB, 5140ms]
DP = [0] * (K + 1)
for cur_object in range(1, N + 1):
    for limit in range(K, 0, -1):   # 그래야지 DP[cur_object-1][]값을 유효하게 참조할 수 있다.
        if limit >= weight[cur_object]:
            DP[limit] = max(DP[limit], DP[limit-weight[cur_object]] + value[cur_object])
print(DP[-1])

# [3]. 메모이제이션 [139MB, 3048ms]
# memoization 할 필요가 없음. 상태공간이 겹칠 확률이 매우 적기는 하다.
def memoization(i, j):
    if i <= 0 or j <= 0:    # 베이스 반환 조건
        return 0
    if DP[i][j]:            # 저장된 DP값이 있으면, 해당 값을 반환
        return DP[i][j]
    # 메인 아이디어 코드
    if j >= weight[i]:      # n번째 물건의 무게가 배낭의 최대 무게 이하면
        DP[i][j] = max(memoization(i-1, j), memoization(i-1, j-weight[i]) + value[i])   # 물건을 배낭에 넣지 않거나, 물건 무게 만큼 비우고 물건을 넣는 경우 중 가치가 큰것을 선택한다.ㄹ
    else:                   # n번째 물건의 무게가 배낭의 최대 무게보다 크면
        DP[i][j] = memoization(i-1, j)  # 물건을 배낭에 넣지 않는다.
    return DP[i][j]

DP = [[0] * (K + 1) for _ in range(N + 1)]
print(memoization(N, K))

# [4]. 메모이제이션 없는 재귀호출 [시간초과]
def recursive(i, j):
    if i <= 0 or j <= 0:
        return 0
    if j >= weight[i]:
        return max(recursive(i-1, j), recursive(i-1, j-weight[i]) + value[i])
    else:
        return recursive(i-1, j)

print(recursive(N, K))
