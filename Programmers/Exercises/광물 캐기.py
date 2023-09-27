STRESS = [
    {
        "diamond": 1,
        "iron": 1,
        "stone": 1,
    },
    {
        "diamond": 5,
        "iron": 1,
        "stone": 1,
    },
    {
        "diamond": 25,
        "iron": 5,
        "stone": 1,
    },
]


def backtracking(N, n, picks, M, minerals, stress):
    global answer

    # pruning
    if stress > answer - 1:
        return

    # end condtion
    if n == N or 5 * n > M - 1:
        answer = min(answer, stress)
        return stress

    # traverse
    for i in range(3):
        if not picks[i]:
            continue

        picks[i] -= 1
        new_stress = stress
        for j in range(5 * n, min(5 * (n + 1), M)):
            mineral = minerals[j]
            new_stress += STRESS[i][mineral]

        backtracking(N, n + 1, picks, M, minerals, new_stress)
        picks[i] += 1


def solution(picks, minerals):
    global answer
    answer = 25 * 51

    P = sum(picks)
    M = len(minerals)

    backtracking(P, 0, picks, M, minerals, 0)

    return answer
