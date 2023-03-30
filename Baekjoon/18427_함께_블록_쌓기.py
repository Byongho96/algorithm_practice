if __name__ == "__main__":
    NUM_STUDENT, MAX_BLOCKS, HEIGHT = map(int, input().split())

    # 2차원 DP
    # 가로 행: 학생 수
    # 세로 행: 높이
    DP = [ [0] * (NUM_STUDENT + 1) for _ in range(HEIGHT + 1)]
    DP[0] = [1] * (NUM_STUDENT + 1)

    blocks = [list(map(int, input().split())) for _ in range(NUM_STUDENT) ] # 학생이 가진 블록 정보 리스트로 입력
 
    for height in range(1, HEIGHT + 1):
        for student in range(1, NUM_STUDENT + 1):
            DP[height][student] = DP[height][student-1] # 학생이 블록을 안 쌓을 경우
            for block in blocks[student - 1]:           # 학생이 블록을 쌓을 경우
                DP[height][student] += (DP[height-block][student-1] if height >= block else 0)

    answer = DP[-1][-1] % 10007

    print(answer)