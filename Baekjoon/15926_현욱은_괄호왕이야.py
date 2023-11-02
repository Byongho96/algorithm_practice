import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    string = input()

    # list for logging the data
    count_log = [0] * N

    mx = 0
    stack = []
    for i in range(N):
        c = string[i]
        if c == "(":
            stack.append(i)
        elif stack:
            si = stack.pop()
            count_log[i] = i - si + 1 + count_log[si - 1]
            mx = max(mx, count_log[i])

    print(mx)
