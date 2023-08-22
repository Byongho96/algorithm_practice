# num of killed enemies
def cal_killed_enemies(archers):
    # simulate
    enemies_set = set(enemies)
    killed_enemies = 0
    for move in range(N):
        # move forward
        reached_enemies = set()
        for ei, ej in enemies_set:
            if ei + move > N - 1:
                reached_enemies.add((ei, ej))
        enemies_set -= reached_enemies
        if len(enemies_set) == 0:
            return killed_enemies 
        
        # target enemies
        target_enemies = set()
        for aj in range(M):
            if not archers[aj]:
                continue
            min_dis = N + M
            min_enemy = None
            for ei, ej in enemies_set:
                dis = abs(N - ei - move) + abs(aj - ej)
                if dis > D:
                    continue
                elif dis < min_dis:
                    min_dis = dis
                    min_enemy = (ei, ej)
                elif dis == min_dis and ej < min_enemy[1]:
                    min_enemy = (ei, ej)
            if min_enemy:
                target_enemies.add(min_enemy)

        # attack enemies
        enemies_set -= target_enemies
        killed_enemies += len(target_enemies)
        if killed_enemies == E:
            return killed_enemies 
        
    return killed_enemies 


# bakctracking
def backtracking_combinations(n, i, archers):
    global answer

    # pruning
    if answer == E:
        return

    # end condition
    if n == 3:
        result = cal_killed_enemies(archers)
        if result > answer:
            answer = result
        return

    # candidate cases
    for j in range(i, M):
        if archers[j]:
            continue
        archers[j] = True
        backtracking_combinations(n + 1, j + 1, archers)
        archers[j] = False

if __name__ == '__main__':
    # row, column, archer distance
    N, M, D = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # total enemies
    enemies = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                enemies.append((i, j))
    E = len(enemies)

    # run backtracking
    answer = 0
    archers = [False] * M
    backtracking_combinations(0, 0, archers)

    # print the result
    print(answer)