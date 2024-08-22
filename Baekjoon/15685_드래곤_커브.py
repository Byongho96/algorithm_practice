import sys
input = sys.stdin.readline

MAX = 100

def count_dragon_square(arr):
    cnt = 0
    for i in range(MAX):
        for j in range(MAX):
            if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
                cnt += 1
    return cnt


def solution(N, dragon_curve):
    arr = [[0] *(MAX + 1) for _ in range(MAX + 1)]
    direction = ((0, 1), (-1, 0), (0, -1), (1, 0))

    for x, y, d, g in dragon_curve:
        # 0세대 생성
        arr[y][x] = 1
        arr[y + direction[d][0]][x + direction[d][1]] = 1
        points = [(y, x) , (y + direction[d][0], x + direction[d][1])]

        for _ in range(g):
            pivot = points[-1]
            for i, j in [*points[-2::-1]]:
                # 90도 회전
                new_i = j - (pivot[1] - pivot[0])
                new_j = -i + (pivot[0] + pivot[1])

                arr[new_i][new_j] = 1
                points.append((new_i, new_j))
        

    return count_dragon_square(arr)


if __name__ == "__main__":
    N = int(input())
    dragon_curve = [map(int, input().split()) for _ in range(N)]

    answer = solution(N, dragon_curve)
    print(answer)