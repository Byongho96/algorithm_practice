def sudokuVerify(sdk):
    std = [0] + [1] * 9

    # 행검사 -> 열검사
    for _ in range(2):
        for i in range(9):
            count = [0] * 10
            for j in range(9):
                count[sdk[i][j]] += 1
            if count != std:
                return 0
        sdk = list(zip(*sdk))

    # 소그룹 검사
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            count = [0] * 10
            for di in range(3):
                for dj in range(3):
                    count[sdk[i+di][j+dj]] += 1
            if count != std:
                return 0
    return 1

T = int(input())

for t in range(1, T+1):
    sdk = [list(map(int, input().split())) for _ in range(9)]
    result = sudokuVerify(sdk)
    print(f'#{t} {result}')
