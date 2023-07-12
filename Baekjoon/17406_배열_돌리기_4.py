def calculate_arr_value(ordered_commands):
    global arr, N, M, min_value

    # 깊은 복사 수행. deepcopy보다 그냥 직접 복사가 더 빠름 748 -> 364
    arr_copy = [row[:] for row in arr]
    
    # 시계방향으로 이동 구현
    for r, c, s in ordered_commands:
        r -= 1  # 인덱스와 동기화
        c -= 1  # 인덱스와 동기화
        for d in range(1, s + 1):
            right_top_corner = arr_copy[r-d][c+d]
            arr_copy[r-d][c-d+1:c+d+1] = arr_copy[r-d][c-d:c+d]  # 오른쪽 이동
            for row in range(r-d, r+d):  # 위로 이동
                arr_copy[row][c-d] = arr_copy[row+1][c-d]
            arr_copy[r+d][c-d:c+d] = arr_copy[r+d][c-d+1:c+d+1] # 왼쪽 이동
            for row in range(r+d, r-d, -1):  # 아래 이동
                arr_copy[row][c+d] = arr_copy[row-1][c+d]
            arr_copy[r-d+1][c+d] = right_top_corner

    for row in arr_copy:
        min_value = min(min_value, sum(row))

    return min_value


def iterate_backtracking(n, used_commands, ordered_commands):
    global commands

    # 종료조건
    if n == K:
        calculate_arr_value(ordered_commands)
        return
    
    # 후보군 출력
    for i in range(K):
        if not used_commands[i]:
            used_commands[i] = True
            ordered_commands[n] = commands[i]
            iterate_backtracking(n + 1, used_commands, ordered_commands)
            used_commands[i] = False
    return

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    commands = [list(map(int, input().split())) for _ in range(K)]

    min_value = 50 * 100    # 결과 저장
    used_commands = [False] * K # 순서 백트래킹(permutations)을 위한 배열
    ordred_commands = [[] for _ in range(K)]    # 순서대로 커맨드를 담을 배열
    iterate_backtracking(0, used_commands, ordred_commands)

    print(min_value)