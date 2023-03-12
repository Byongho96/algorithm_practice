import sys
input = sys.stdin.readline

def divide_conquer(size, si, sj):
    # 베이스 리턴문 작성
    if size == 1:
        return arr[si][sj]
    # 재귀호출(divide) 및 반환값 처리(Conquer)
    half = size // 2
    mi = si + half
    mj = sj + half
    lst = [divide_conquer(half, si, sj), divide_conquer(half, mi, sj), divide_conquer(half, si, mj), divide_conquer(half, mi, mj)]
    lst.sort()
    return lst[2]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(divide_conquer(N, 0, 0))
