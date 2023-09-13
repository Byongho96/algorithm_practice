answer = 0


def backtracking(n, weak, dist, W):
    global answer

    # pruning
    if n > answer - 1:
        return

    # end condition
    if not sum(weak):
        answer = min(answer, n)
        return

    # traverse candidates
    coverage = dist[n]
    for s in range(W):
        if not weak[s]:
            continue
        new_weak = weak[:]
        e = s
        sm = weak[s]
        cnt = 0
        while sm < coverage and cnt < W:
            new_weak[s] = 0
            e = e + 1 if e + 1 < W else e + 1 - W
            sm += weak[e]
            cnt += 1
        sm -= weak[e]
        new_weak[s - 1] = 0
        new_weak[e] = 0
        backtracking(n + 1, new_weak, dist, W)


def solution(n, weak, dist):
    global answer

    W = len(weak)
    D = len(dist)

    # max_answer
    max_answer = min(D, W // 2 + 2)
    answer = max_answer

    # make weak point difference array
    weak_diff = [0] * n
    for i in range(1, W):
        weak_diff[i] = weak[i] - weak[i - 1]
    weak_diff[0] = weak[0] + n - weak[-1]

    # sort dist in reverse order
    dist.sort(reverse=True)

    # backtracking
    backtracking(0, weak_diff, dist, W)

    if answer == max_answer:
        return -1
    return answer


if __name__ == "__main__":
    print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
    print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
