import sys
from typing import List
input = sys.stdin.readline

def calculate_taste(cum_arr: List[List[int]], si: int, sj: int, ei: int, ej: int) -> int | List[str]:
    return (cum_arr[ei][ej] - cum_arr[ei][sj - 1] - cum_arr[si - 1][ej] + cum_arr[si - 1][sj - 1]) - (cum_arr[ei - 1][ej - 1] - cum_arr[ei - 1][sj] - cum_arr[si][ej - 1] + cum_arr[si][sj])

def is_available_ring(arr: List[List[int]], si: int, sj: int, ei: int, ej:int) -> List[List[int]]:
    for i in range(si - 1, ei):
        if arr[i][sj - 1] == 101 or arr[i][ej - 1] == 101:
            return False
    for j in range(sj - 1, ej):
        if arr[si - 1][j] == 101 or arr[ei - 1][j] == 101:
            return False
    return True

def peel_the_ring(arr: List[List[int]], si: int, sj: int, ei: int, ej:int) -> List[List[int]]:
    for i in range(si - 1, ei):
        arr[i][sj - 1] = 101
        arr[i][ej - 1] = 101
    for j in range(sj - 1, ej):
        arr[si - 1][j] = 101
        arr[ei - 1][j] = 101

def solution(N: int, M: int, arr: List[List[int]]) -> int:
    # cumlative sum
    cum_arr = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cum_arr[i][j] += arr[i - 1][j - 1] + cum_arr[i][j - 1] + cum_arr[i - 1][j] - cum_arr[i - 1][j - 1]
    
    # get all the possible onion rings
    rings = []
    for si in range(1, N - 1):
        for sj in range(1, N -1):
            for ei in range(si + 2, N + 1):
                for ej in range(sj + 2, N + 1):
                    rings.append([calculate_taste(cum_arr, si, sj, ei, ej), si, sj, ei, ej])

    # sort possible rings
    rings.sort(key=lambda x: x[0], reverse=True)
                    
    # peel the rings
    peeled_rings: List[str] = []
    for [taste, si, sj, ei, ej] in rings:
        if not is_available_ring(arr, si, sj, ei, ej):
            continue
        peeled_rings.append(f'{taste} {si} {sj} {ei} {ej}')
        peel_the_ring(arr, si, sj, ei, ej)
        if len(peeled_rings) == M:
            break

    return peeled_rings if len(peeled_rings) == M else 0

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = solution(N, M, arr)
    if (answer):
        print(*answer, sep='\n')
    else:
        print(0)