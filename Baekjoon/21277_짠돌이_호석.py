# 90도 회전 시키는 함수
def rotate_90(lst, st):
    N = len(lst)
    M = len(lst[0])

    result_lst = [ [0] * N for _ in range(M) ]

    for i in range(N):
        for j in range(M):
            result_lst[j][N-i-1] = lst[i][j]

    result_set = set(map(lambda point: (point[1], N - point[0] - 1), st))

    return (result_lst, result_set)

if __name__ == "__main__":

    # 퍼즐 1 입력받기
    N1, M1 = map(int, input().split())
    puzzle_1 = [ list(map(int, input())) for _ in range(N1) ]

    # 퍼즐 1 집합으로 만들기
    set_1 = set()
    for i in range(N1):
        for j in range(M1):
            if puzzle_1[i][j]:
                set_1.add((i, j))
    num_puzzle_1 = len(set_1)

    # 퍼즐 2 입력받기
    N2, M2 = map(int, input().split())
    puzzle_2 = [ list(map(int, input())) for _ in range(N2) ]

    # 퍼즐 2 집합으로 만들기
    set_2 = set()
    for i in range(N2):
        for j in range(M2):
            if puzzle_2[i][j]:
                set_2.add((i, j))
    num_puzzle_2 = len(set_2)

    mn = (N1 + N2) * (M1 + M2)  # 주의) 이론상 최댓값은 대각선으로 놓일 때!!

    # 퍼즐2를 90도씩 돌려가며 반복
    for _ in range(4):
        # 퍼즐2가 퍼즐1 위를 한칸씩 올겨가며 순환하는 형태
        for i in range(-N2 + 1, N1 + 1):
            for j in range(-M2 + 1, M1 + 1):
                # 집합 연산자로 겹치는게 있는지 판별
                moved_set_2 = set(map(lambda point: (point[0] + i, point[1] + j), set_2))
                intersection_set = set_1.intersection(moved_set_2)
                if not intersection_set:
                    area = (max(N1, N2 + i) - min(0, i)) * (max(M1, M2 + j) - min(0, j))
                    mn = min(mn, area)

        # 퍼즐2 90도 돌리기
        puzzle_2, set_2 = rotate_90(puzzle_2, set_2)
        N2, M2 = M2, N2

    print(mn)