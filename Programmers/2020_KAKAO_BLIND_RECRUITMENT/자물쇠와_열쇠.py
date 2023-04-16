def rotate_90(i_j_set, M):
    new_set = set()
    for i, j in i_j_set:
        new_set.add((j, M-i-1))
    return new_set

def solution(key, lock):
    N = len(lock[0])
    M = len(key[0])
    
    # 자물쇠에서 필요한 (i, j)값
    not_demand_set = set()
    demand_set = set()
    for i in range(N):
        for j in range(N):
            if lock[i][j]:
                not_demand_set.add((i, j))
            else:
                demand_set.add((i, j))
             
    # 열쇠가 제공할 수 있는 (i, j)값
    supply_set = set()
    for i in range(M):
        for j in range(M):
            if key[i][j]:
                supply_set.add((i, j))
                
    for _ in range(4):  # 90도씩 돌리면서 4번 반복
        for i in range(-M + 1, N):
            for j in range(-M + 1, N):
                moved_set = set(map(lambda point: (point[0] + i, point[1] + j), supply_set))
                if demand_set.issubset(moved_set) and not not_demand_set.intersection(moved_set):
                    return True
        supply_set = rotate_90(supply_set, M)
    
    return False