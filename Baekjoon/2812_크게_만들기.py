if __name__ == "__main__":
    N, K = map(int, input().split())
    nums = list(map(int, input()))

    k = K
    stack = []
    for num in nums:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    print("".join(map(str, stack[: N - K])))
