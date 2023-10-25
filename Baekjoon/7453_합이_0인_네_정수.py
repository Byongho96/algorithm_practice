import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # Group two arrays to create a sum array
    sum_arr = [[], []]
    for i in range(N):
        for j in range(N):
            sum_arr[0].append(arr[i][0] + arr[j][1])
            sum_arr[1].append(arr[i][2] + arr[j][3])

    # Sort the arrays for two poiner
    sum_arr[0].sort()
    sum_arr[1].sort()

    # Run two pointer
    answer = 0
    s, e = 0, N**2 - 1
    while s < N**2 and e > -1:
        result = sum_arr[0][s] + sum_arr[1][e]

        # If find the case
        if result == 0:
            # count on the first array
            A = sum_arr[0][s]
            a = 0
            while s < N**2 and sum_arr[0][s] == A:
                s += 1
                a += 1

            # count on the second array
            B = sum_arr[1][e]
            b = 0
            while e > -1 and sum_arr[1][e] == B:
                e -= 1
                b += 1

            # update answer
            answer += a * b

        # If the result is bigger than zero
        elif result > 0:
            e -= 1

        # If the result is smaller than zero
        else:
            s += 1

    print(answer)
