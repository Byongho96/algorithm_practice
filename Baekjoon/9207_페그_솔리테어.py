import sys
from typing import List, Tuple

sys = sys.stdin.readline

DIRECTION = ((1, 0), (-1, 0), (0, 1), (0, -1))

def backtracking(total: int, arr: List[List[str]], removed: int, pins: List[Tuple[str]]) -> int:
    # pruning
    if not pins:
        return removed

    # end condition
    if removed == total - 1:
        return removed

    # traverse candidates
    mx = removed
    for idx, (pi, pj) in enumerate(pins):
        for di, dj in DIRECTION:
            ti = pi + di; tj = pj + dj  # target pin poistion
            ji = ti + di; jj = tj + dj  # target jump position
            
            # filter invalid condition
            if  ji < 0 or ji > 4 or jj < 0 or jj > 8:
                continue
            if arr[ti][tj] != 'o' or arr[ji][jj] != '.':
                continue

            # jump the pin
            arr[pi][pj] = '.'
            arr[ti][tj] = '.'
            arr[ji][jj] = 'o'
            new_pins = pins[:]
            new_pins.pop(idx)
            new_pins.remove((ti, tj))
            new_pins.append((ji, jj))

            # update the maximum
            mx = max(backtracking(total, arr, removed + 1, new_pins), mx)
            if mx == total - 1:
                return mx
            
            # restore the info
            arr[pi][pj] = 'o'
            arr[ti][tj] = 'o'
            arr[ji][jj] = '.'

    return mx
    
def solution(arr: List[List[str]]) -> List[int]:
    # extract the pin info
    total = 0
    pins = []
    for i in range(5):
        for j in range(9):
            if arr[i][j] == 'o':
                total += 1
                pins.append((i, j))

    # run backtracking
    max_removed = backtracking(total, arr, 0, pins)

    # return the answer
    return [total - max_removed, max_removed]


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        arr = [list(input().rstrip())for _ in range(5)]

        answer = solution(arr)
        print(*answer)
        
        if t != T - 1:
            input()
