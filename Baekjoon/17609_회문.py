import sys

input = sys.stdin.readline


def check_palindrome(string: str, offset: int):
    N = len(string)

    if not string:
        return 0 if offset else 1

    start, end = -1, N
    for _ in range(N // 2):
        start += 1
        end -= 1

        if string[start] == string[end]:
            continue
        if not offset or start + 1 == end:
            return 2

        return min(
            check_palindrome(string[start + 1 : end + 1], 0),
            check_palindrome(string[start:end], 0),
        )

    return 0 if offset else 1


if __name__ == "__main__":
    results = [check_palindrome(input().rstrip(), 1) for _ in range(int(input()))]
    print(*results, sep="\n")
