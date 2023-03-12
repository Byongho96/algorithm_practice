import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def combination(i, sm):
    global result
    # 종료조건
    if sm >= B:
        result = min(result, sm)
        return
    # 가지치기
    if sm >= result:
        return
    # 조합형성
    for j in range(i, N):               # i번째 인덱스의 사람부터 모두 탐색
        combination(j + 1, sm+height[j])    # i번째 인덱스의 사람이 참여한 경우
                                            # 안 한 경우는 굳이 고려 X, 어차피 for문으로 돌 것임

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    result = sum(height)
    # used = [0] * N
    combination(0, 0)

    print(f'#{tc} {result - B}')