import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    # answer array
    answers = [-1] * N

    # using stack
    stack = []
    for idx in range(N):
        num = nums[idx]
        while stack and num > stack[-1][0]:
            n, i = stack.pop()
            answers[i] = num
        stack.append((num, idx))

    print(*answers)
