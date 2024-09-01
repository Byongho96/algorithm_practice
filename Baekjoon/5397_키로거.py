import sys
input = sys.stdin.readline

def solution(N, passwords):
    answers = []

    for password in passwords:
        left = []
        right = []

        for p in password:
            if p == "<":
                if left:
                    right.append(left.pop())
            elif p == ">":
                if right:
                    left.append(right.pop())
            elif p == "-":
                if left:
                    left.pop()
            else:
                left.append(p)

        answers.append(''.join(left) + ''.join(right[::-1]))

    return answers


if __name__ == "__main__":
    N = int(input())
    passwords = [list(input().rstrip()) for _ in range(N)]

    answer = solution(N, passwords)
    print(*answer, sep='\n')