import sys
input = sys.stdin.readline

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

# 학생 배치
def dis_students(arr, student, crushed_students):
    # 1. 좋아하는 학생이 인접한 칸에 가장 많은 칸
    max_seats = []
    max_score = 0
    flag = False
    # 자리에 대한 점수 계산
    for i in range(1, N + 1):
        if flag:
            break
        for j in range(1, N + 1):
            if arr[i][j]:
                continue
            score = 0
            # 좋아하는 학생 자리일 경우, 그 주변 자리에 점수 + 1
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if arr[ni][nj] in crushed_students:
                    score += 1
            # 최대 점수와 최대 점수 자리 업데이트
            if score == 4:
                max_seats = [(i, j)]
                flag = True
                break
            if score > max_score: 
                max_score = score
                max_seats = [(i, j)]
            elif score == max_score:
                max_seats.append((i, j))

    # 1번으로 끝 날 경우
    if len(max_seats) == 1:
        i, j = max_seats[0]
        arr[i][j] = student
        return

    # 2. 비어있는 칸이 인접한 칸에 가장 많은 칸
    second_max_seats = []
    second_max_score = 0

    # 2-1. 이전 단계에서의 결과가 하나 이상인 경우
    if len(max_seats) > 0:
        max_seats.sort()
        for i, j in max_seats:
            score = 0
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if arr[ni][nj] == 0:
                    score += 1
            # 최대 스코어 계산
            if score == 4:
                second_max_seats = [(i, j)]
                break
            if score > second_max_score:
                second_max_score = score
                second_max_seats = [(i, j)]
            elif score == second_max_score:
                second_max_seats.append((i, j))
    
    # 2-2. 이전 단계에서 결과가 하나도 안나온 경우
    else:
        flag = False
        for i in range(1, N + 1):
            if flag:
                break
            for j in range(1, N + 1):
                # 이미 차지된 자리 통과
                if arr[i][j]:
                    continue
                score = 0
                for idx in range(4):
                    ni = i + di[idx]
                    nj = j + dj[idx]
                    if arr[ni][nj] == 0:
                        score += 1
                # 최대 스코어 계산
                if score == 4:
                    second_max_seats = [(i, j)]
                    flag = True
                    break
                if score > second_max_score:
                    second_max_score = score
                    second_max_seats = [(i, j)]
                elif score == second_max_score:
                    second_max_seats.append((i, j))

    # 3. 행, 열의 번호가 가장 작은 칸
    second_max_seats.sort()
    i, j = second_max_seats[0]
    arr[i][j] = student
    return

# 총 점수 계산
def cal_score(arr, info):
    total_score = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            student = arr[i][j]
            crushed_students = info[student]
            # 해당 학생 점수 계산
            score = 0
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if arr[ni][nj] in crushed_students:
                    score += 1
            # 총 점수 업데이트
            if score:
                total_score += 10 ** (score - 1)
    return total_score

if __name__ == '__main__':
    N = int(input())

    # Seats
    arr = [[-1] * (N + 2)] + [[-1] + [0] * N + [-1] for _ in range(N)] + [[-1] * (N + 2)]

    # Distrubute Students
    info = [[] for _ in range(N * N + 1)]
    for _ in range(N * N):
        i, j1, j2, j3, j4 = map(int, input().split())
        info[i].extend([j1, j2, j3, j4])
        dis_students(arr, i, [j1, j2, j3, j4])

        # print(arr)
    # Calculate score
    score = cal_score(arr, info)
    print(score)