import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, P = map(int, input().split())

    answer = 0
    stacks = [[0] for _ in range(7)]  # set the highest fret

    for _ in range(N):
        n, p = map(int, input().split())
        # take finger off
        while p < stacks[n][-1]:
            stacks[n].pop()
            answer += 1
        # press
        if p > stacks[n][-1]:
            stacks[n].append(p)
            answer += 1

    print(answer)
