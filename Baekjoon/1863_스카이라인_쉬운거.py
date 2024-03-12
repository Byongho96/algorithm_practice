import sys
from typing import List, Tuple

input = sys.stdin.readline

def solution(N: int, skyline: List[int]):
    cnt = 0
    stack = [0]

    for height in skyline:   
        # skyline height increased 
        if height > stack[-1]:
            stack.append(height)
            cnt += 1
            continue

        # skyline height decreased 
        while stack[-1] > height:
            stack.pop()

        # check the ommited building on decreasing
        if height != stack[-1]:
            stack.append(height)
            cnt += 1

    return cnt


if __name__ =="__main__":
    # get inputs
    N = int(input())
    skyline = list(int(input().split()[1]) for _ in range(N))
    
    # print answer
    answer = solution(N, skyline)
    print(answer)