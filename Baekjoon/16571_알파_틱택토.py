'''
0 -> 패배
1 -> 동점
2 -> 승리
'''

# 승패 판정 함수
def isWin(board, player):
    board_trans = list(zip(*board))
    diagonal_1 = 0
    diagonal_2 = 0
    for i in range(3):
        if board[i].count(player) == 3 or board_trans[i].count(player) == 3:
            return True
        if board[i][i] == player:
            diagonal_1 += 1
        if board[i][2-i] == player:
            diagonal_2 += 1
    if diagonal_1 == 3 or diagonal_2 == 3:
        return True
    return False

# 백트래킹 함수 (내 차례에서 항상 최선의 결과를 반납)
def backtracking(N, step, board, first, second):

    current = first
    previous = second
    if step % 2:
        current = second
        previous = first

    # 종료조건1: 승패 판정
    if isWin(board, previous):
        return 0
    
    # 종료조건2: 게임이 더 진행될 수 없는 경우
    if N == step:
        return 1

    # 내가 둘 수 있는 경우의 수 중 최선을 결과를 return
    best_result = 0
    for n in range(9):
        i, j = divmod(n, 3)
        if not board[i][j]:
            board[i][j] = current
            result = 2 - backtracking(N, step + 1, board, first, second)  # 다음 턴에서 상대 플레이어가 2(이김), 1(비김), 0(짐) -> 나는 0(짐), 1(비김), 2(이김) 
            board[i][j] = 0
            best_result = max(best_result, result)
            if best_result == 2:
                break

    return best_result

if __name__ == "__main__":

    board = [list(map(int, input().split())) for _ in range(3)]

    num_1 = 0
    num_2 = 0
    for i in range(3):
        num_1 += board[i].count(1)
        num_2 += board[i].count(2)

    first = 1
    second = 2
    if num_1 > num_2:
        first = 2
        second = 1

    result = backtracking(9 - num_1 - num_2, 0, board, first, second)

    print( 'W' if result == 2 else 'D' if result == 1 else 'L' )
