import sys
input = sys.stdin.readline

def isPromising(sudoku, i, j, num):
    # check row
    if num in sudoku[i]:
        return False
    
    # check column
    for idx in range(9):
        if sudoku[idx][j] == num:
            return False
        
    # check square
    si = i // 3
    sj = j // 3
    for ni in range(3 * si, 3 * si  + 3):
        for nj in range(3 * sj, 3 * sj  + 3):
            if sudoku[ni][nj] == num:
                return False
    
    return True


def backtracking(N, n, sudoku, empty):
    global is_completed
    global answer

    # pruning
    if is_completed:
        return

    # end condition
    if N == n:
        is_completed = True
        for row in sudoku:
            answer.append(row[:])
        return

    # candidate cases
    i, j = empty[n]
    for num in range(1, 10):
        if not isPromising(sudoku, i, j, num):
            continue
        sudoku[i][j] = num
        backtracking(N, n + 1, sudoku, empty)
        sudoku[i][j] = 0

if __name__ == '__main__':
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # count empty spots
    empty = []
    for i in range(9):
        for j in range(9):
            if not sudoku[i][j]:
                empty.append((i, j))

    # backtracking
    answer = []
    N = len(empty)
    is_completed = False
    backtracking(N, 0, sudoku, empty)

    for row in answer:
        print(*row)