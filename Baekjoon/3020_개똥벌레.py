import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, H = map(int, input().split())

    # cumulative data for time efficiency
    cul_obstacles = [0 for _ in range(H + 1)]
    reverse_cul_obstacles = [0 for _ in range(H + 1)]

    # record the info
    for i in range(N):
        length = int(input())
        if i % 2:
            reverse_cul_obstacles[H - length + 1] += 1
        else:
            cul_obstacles[length] += 1

    # cumulate the array
    for i in range(2, H + 1):
        cul_obstacles[H - i + 1] += cul_obstacles[H - i + 2]
        reverse_cul_obstacles[i] += reverse_cul_obstacles[i - 1]

    mn = N
    mn_cnt = 0
    for i in range(1, H + 1):
        obstacles = cul_obstacles[i] + reverse_cul_obstacles[i]
        if obstacles < mn:
            mn = obstacles
            mn_cnt = 1
        elif obstacles == mn:
            mn_cnt += 1

    print(mn, mn_cnt)
