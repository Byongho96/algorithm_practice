import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def brute_force(i, j, n, string):
    # 종료조건
    if n == 7:
        nums.add(string)
        return
    # 가지치기

    # 후보군 출력
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni = i + di
        nj = j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
        # if 0 <= ni < 4 and 0 <= nj < 4 and (n, string) not in record[ni][nj]:
        #     record[ni][nj].append((n, string))  # 가지치기용 기록. arr[ni][nj] 위치에 (n번째, string) 정보를 갖고 들어왔었다.
            brute_force(ni, nj, n+1, string + arr[ni][nj])

    # 가지치기 같은 위치에 동일한 기록으로 접근

T = int(input())

for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]

    nums = set()
    # record = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            brute_force(i, j, 0, '')
    result = len(nums)

    print(f'#{tc} {result}')