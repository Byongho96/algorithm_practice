import sys
input = sys.stdin.readline

def cutting_by(middle):
    result = 0
    for line in lines:
        result += line // middle
    return result

if __name__ == "__main__":
    K, N = map(int, input().split())
    lines = [0] * K
    for i in range(K):
        lines[i] = int(input())

    start = 0
    end = 2 ** 31 - 1
    while start <= end:                 # 이분탐색 진행
        middle = (start + end) // 2
        num = cutting_by(middle)        # middle의 길이로 잘랐을 때, 만들어지는 랜선의 수
        if num >= N:
            start = middle + 1
        if num < N:
            end = middle - 1
    print(end)