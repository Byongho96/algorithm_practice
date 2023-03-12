import sys
input = sys.stdin.readline


def divide_conquer(si, sj, size):
    global one, zero
    # 베이스 리턴문 작성
    if size == 1:
        return arr[si][sj]
    # 재귀호출(divide) 및 반환값 처리(Conquer)
    half = size // 2
    mi = si + half
    mj = sj + half

    def adding(result):
        nonlocal half
        nonlocal tmp_one, tmp_zero
        if result == 1:
            tmp_one += 1
        elif result == 0:
            tmp_zero += 1
    tmp_one = 0
    tmp_zero = 0
    adding(divide_conquer(si, sj, half))
    adding(divide_conquer(mi, sj, half))
    adding(divide_conquer(si, mj, half))
    adding(divide_conquer(mi, mj, half))

    if tmp_one == 4:
        return 1
    elif tmp_zero == 4:
        return 0
    else:
        one += tmp_one
        zero += tmp_zero
        return None

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

one = 0
zero = 0
result = divide_conquer(0, 0, N)
if result == 1:
    one = 1
elif result == 0:
    zero = 1
print(zero, one, sep='\n')

