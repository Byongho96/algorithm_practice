import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def backtracking(n, cur):
    global mx, mn
    if n == N - 1:
        mx = max(mx, cur)
        mn = min(mn, cur)
        return
    num = nums[n + 1]
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            if i == 0:
                nex = cur + num
            elif i == 1:
                nex = cur - num
            elif i == 2:
                nex = cur * num
            else:
                nex = int(cur / num)
                # 밑에 경우는 -9 / 9 읙
                # if cur >= 0:
                #     nex = cur // num
                # else:
                #     nex = cur // num + 1
            backtracking(n + 1, nex)
            operator[i] += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    mx = -100000000
    mn = 100000000
    backtracking(0, nums[0])

    result = mx - mn
    print(f'#{tc} {result}')