import sys
from collections import Counter
input = sys.stdin.readline

def something(N, arr, jump, cnt):
    i = 1
    while i < N + 1:
        arr[i] += cnt
        i += jump

def solution(N, K, jumps, checks):
    arr = [0] * (N + 1)
    
    # 카운터
    counter = Counter(jumps)
    
    # 점프 실행
    for jump, cnt in counter.items():
        something(N, arr, jump, cnt)

    # 누적합
    for i in range(2, N + 1):
        arr[i] += arr[i - 1]

    # 답안 출력
    answer = []
    for l, r in checks:
        answer.append(arr[r + 1] - arr[l])

    return answer

if __name__ == "__main__":
    N, K = map(int, input().split())
    jumps = tuple(map(int, input().split()))
    checks = tuple(tuple(map(int, input().split())) for _ in range(int(input())))

    answer = solution(N, K, jumps, checks)
    print(*answer, sep='\n')