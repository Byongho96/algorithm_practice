def is_promising(N, num):
    for unit in range(1, N // 2 + 1):
        if num[N - 2 * unit : N - unit] == num[N - unit : N]:
            return False

    return True


def print_min_good_sequence(N, n, result):
    # end condition
    if n == N:
        print(result)
        exit()

    # traverse the candidates
    for i in "123":
        num = result + i
        if is_promising(n + 1, num):
            print_min_good_sequence(N, n + 1, num)

    return result


if __name__ == "__main__":
    N = int(input())
    print_min_good_sequence(N, 1, "1")
