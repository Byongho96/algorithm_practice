import sys
input = sys.stdin.readline

def backtracking(m, selected, consumed):
    # end condition
    if m == M:
        print(*selected)
        return

    # candidate cases
    for i in range(S):
        if consumed[i] < max_nums[i]:
            consumed[i] += 1
            selected[m] = nums_set[i]
            backtracking(m + 1, selected, consumed)
            consumed[i] -= 1

if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # sort the nums withouth duplication
    nums_set = list(set(nums))
    nums_set.sort()
    S = len(nums_set)

    # make the max nums arr
    max_nums = [nums.count(num) for num in nums_set]

    # run backtracking
    selected = [0] * M
    consumed = [0] * S
    backtracking(0, selected, consumed)

# def backtracking(nums, M, m, visited, selected):
#     global answers

#     # end condition
#     if m == M:
#         answers.add(tuple(selected))
#         return

#     # candidate cases
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             selected.append(nums[i])
#             backtracking(nums, M, m + 1, visited, selected)
#             visited[i] = False
#             selected.pop()

# if __name__ == '__main__':
#     N, M = map(int, input().split())
#     nums = list(map(int, input().split()))

#     # sort the nums
#     nums.sort()

#     # run backtracking
#     answers = set()
#     visited = [False] * N
#     backtracking(nums, M, 0, visited, [])

#     # print the answer
#     answers = list(answers)
#     answers.sort()
#     for answer in answers:
#         print(*answer)