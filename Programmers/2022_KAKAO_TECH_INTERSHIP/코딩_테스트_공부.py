# problems의 길이가 작은 것으로 보아 완전탐색(백트래킹) 도전 => 시간초과로 메모이제이션 적용
# 새로 배운 것: 배열의 상한값을 정할 수 있다.
def backtracking(cul_cost, alp, cop, problems):
    global max_alp_req
    global max_cop_req
    global max_cost
    global memo
    
    # memo배열을 벗어나지 않도록 상한값 지정
    alp = min(max_alp_req, alp)
    cop = min(max_cop_req, cop)
    
    # 가지 치기
    if cul_cost >= max_cost:
        return cul_cost
    
    # 종료 조건
    if alp == max_alp_req and cop == max_cop_req:
        return cul_cost
    
    # 메모이제이션 읽기
    memo_cost = memo[alp][cop]
    if memo_cost:
        return cul_cost + memo_cost
    
    # 후보군 출력
    min_cost = max_cost
    if alp < max_alp_req:   # 알고력 공부
        min_cost = min(min_cost, backtracking(cul_cost + 1, alp + 1, cop, problems))
    if cop < max_cop_req:   # 코딩력 공부
        min_cost = min(min_cost, backtracking(cul_cost + 1, alp, cop + 1, problems))
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:   # 가능한 문제 풀기
        if alp >= alp_req and cop >= cop_req:
            min_cost= min(min_cost, backtracking(cul_cost + cost, alp + alp_rwd, cop + cop_rwd, problems))
    
    memo[alp][cop] = min_cost - cul_cost  # 메모이제이션 쓰기
    return min_cost
        

def solution(alp, cop, problems):
    global max_alp_req
    global max_cop_req
    global max_cost
    global memo
    
    # max_cost(최대 시간) 계산을 위한 작업
    max_alp_req = 0
    max_cop_req = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp_req = max(max_alp_req, alp_req)
        max_cop_req = max(max_cop_req, cop_req)
    max_cost = abs(max_alp_req - alp) + abs(max_cop_req - cop
                                            
    memo = [[0] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]   # 메모이제이션 배열 생성
    answer = backtracking(0, alp, cop, problems)
        
    return answer