import sys
input = sys.stdin.readline

cnt = 0

def check_perfect_square(arr, i, j, length):
    for row in range(i, i + length):
        for col in range(j, j + length):
            if arr[row][col] != 0:
                return  False
    return True


# 4분할하여 완벽한 정사각형인지 확인하고, 완벽한 정사각형이면 중앙부에 cnt를 대입하여 ㄱ타일을 생성한다.
def divide_conquer(arr, i, j, length):
    global cnt

    if length == 1:
        return
    
    cnt += 1
    length //= 2

    if check_perfect_square(arr, i, j, length):   # 왼쪽 위
        arr[i + length - 1][j + length - 1] = cnt
    if check_perfect_square(arr, i, j + length, length):  # 오른쪽 위
        arr[i + length - 1][j + length] = cnt
    if check_perfect_square(arr, i + length, j, length):  # 왼쪽 아래
        arr[i + length][j + length - 1] = cnt
    if check_perfect_square(arr, i + length, j + length, length):  # 오른쪽 아래
        arr[i + length][j + length] = cnt
    
    divide_conquer(arr, i, j, length)
    divide_conquer(arr, i, j + length, length)
    divide_conquer(arr, i + length, j, length)
    divide_conquer(arr, i + length, j + length, length)
    

def solution(K, x, y):
    global cnt
    cnt = 0

    N = 2 ** K

    arr = tuple([0] * N for _ in range(N))
    arr[y - 1][x - 1] = -1

    divide_conquer(arr, 0, 0, N)
    return arr


if __name__ == "__main__":
    K = int(input())
    x, y = map(int, input().split())

    answer = solution(K, x, y)
    for row in answer[::-1]:
        print(*row)