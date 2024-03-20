import re
from typing import List

"""
submarine pattern : (100~1~|01)~

test1 : 10010111
test2 : 100000000001101
"""

# 100~1~ 정규식 테스트
def test_pattern_1(N: int, sound:str, s:int) -> List[int]:
    next_idx = []
    pattern = r'10(0)+1+'
    
    if s > N - 4:
        return next_idx
    
    flag = False
    for e in range(s + 3, N):
        if not re.fullmatch(pattern, sound[s : e + 1]):
            if flag:
                break
            continue
        flag = True
        next_idx.append(e + 1)

    return next_idx

# 01 정규식 테스트
def test_pattern_2(N: int, sound:str, s:int) -> List[int]:
    next_idx = []
    pattern = r'(01)+'

    if s > N - 2:
        return next_idx
    
    flag = False
    for e in range(s + 1, N, 2):
        if not re.fullmatch(pattern, sound[s : e + 1]):
            if flag:
                break
            continue
        flag = True
        next_idx.append(e + 1)

    return next_idx



def solution(sound: str) -> str:
    N = len(sound)
    start_idx = [0]

    # record the test
    test_record = [[False, False] for _ in range(N)]

    while start_idx:
        idx = start_idx.pop()

        if idx == N:
            return 'SUBMARINE'

        if not test_record[idx][0]:
            test_record[idx][0] = True
            start_idx.extend(test_pattern_1(N, sound, idx))

        if not test_record[idx][1]:
            test_record[idx][1] = True
            start_idx.extend(test_pattern_2(N, sound, idx))

    return 'NOISE'

if __name__ == "__main__":
    sound = input()
    
    answer = solution(sound)
    print(answer)