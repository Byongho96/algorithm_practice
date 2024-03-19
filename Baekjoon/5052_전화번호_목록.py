import sys
from typing import List

input = sys.stdin.readline

def solution(N: int, phones: List[str]) -> str:
    # sort ascending
    phones.sort()

    # check the adjacent numbers
    for i in range(N - 1):
        N = len(phones[i])
        if N -1 < len(phones[i + 1]):
            if phones[i + 1][:N] == phones[i]:
                return 'NO'
            
    return 'YES'


if __name__ =="__main__":
    for _ in range(int(input())):
        N = int(input())
        phones = [input().rstrip() for _ in range(N)]

        answer = solution(N, phones)
        print(answer)