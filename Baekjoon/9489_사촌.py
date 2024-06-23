import sys
input = sys.stdin.readline

def solution(N, M, nums):
    parent = [-1] * (N )

    # make parent array
    par = -1
    for i in range(1, N):
        pre = nums[i - 1]
        cur = nums[i]

        if pre + 1 != cur:
            par += 1

        parent[i] = par

    # find cousin nodes
    cnt = 0
    M_idx = nums.index(M)
    for i in range(1, N):
        if parent[i] == parent[M_idx]:
            continue
        if parent[parent[i]] == parent[parent[M_idx]]:
            cnt += 1

    return cnt


if __name__ == "__main__":
    answers = []
    while True:
        N, M = map(int, input().split())
        if N == 0:
            break
        nums = list(map(int, input().split()))
        answer = solution(N, M, nums)
        answers.append(answer)

    print(*answers, sep='\n')
