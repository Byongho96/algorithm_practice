from typing import List

def solution(N: int, arr: List[int]) -> List[str]:
    cnt = [0] * N
    closest = [N] * N

    # from left to right
    stack = [[0, 0] for _ in range(N)]
    ptr = -1
    for idx in range(N):
        height = arr[idx]
        while ptr > -1 and stack[ptr][0] < height + 1:
            ptr -= 1

        if ptr > -1:
            closest[idx] = stack[ptr][1]

        ptr += 1
        stack[ptr][0] = height
        stack[ptr][1] = idx
        cnt[idx] += ptr

    # from right to left
    ptr = -1
    for idx in range(N - 1, -1, -1):    
        height = arr[idx]
        while ptr > -1 and stack[ptr][0] < height + 1:
            ptr -= 1

        if ptr > -1 and abs(idx - closest[idx]) > stack[ptr][1] - idx: 
            closest[idx] = stack[ptr][1]

        ptr += 1
        stack[ptr][0] = height
        stack[ptr][1] = idx
        cnt[idx] += ptr

    # make answer
    answer = []
    for i in range(N):
        if cnt[i] == 0:
            answer.append(f'0')
        else:
            answer.append(f'{cnt[i]} {closest[i] + 1}') 
    return answer

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    answer = solution(N, arr)
    print(*answer, sep='\n')