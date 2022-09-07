# 68ms
# 이진트리 개념을 바탕으로 한, IQ테스트??
import sys
input = sys.stdin.readline

K = int(input())
nums = list(map(int, input().rstrip().split()))
levels = [[] for _ in range(K)]

def find_level(level, arr):
    N = len(arr)
    mid = N//2
    levels[level].append(arr[mid])
    if N == 1:
        return
    find_level(level + 1, arr[:mid])
    find_level(level + 1, arr[mid+1:])
    return


find_level(0, nums)

for i in range(K):
    print(*levels[i])