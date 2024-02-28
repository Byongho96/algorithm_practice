def received_towers(N, towers):
    received = [0] * N
    stack = []

    for i in range(N):
        while stack and stack[-1][0] < towers[i]:
            stack.pop()

        received[i] = stack[-1][1] if stack else 0
        stack.append((towers[i], i + 1))

    return received

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    print(*received_towers(N, arr))