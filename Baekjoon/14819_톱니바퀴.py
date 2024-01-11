import sys

input = sys.stdin.readline

if __name__ == "__main__":
    arr = [list(map(int, input().rstrip())) for _ in range(4)]

    pointer = [0] * 4
    for _ in range(int(input())):
        num, direction = map(int, input().split())
        num -= 1
        pointer[num] -= direction  # rotate

        # left
        # left[2] & cur[6]
        cnt = 1
        while num - cnt > -1:
            left_pole = arr[num - cnt][(pointer[num - cnt] + 2) % 8]
            cur_pole = arr[num - cnt + 1][
                (pointer[num - cnt + 1] - direction * (-1) ** cnt + 6) % 8
            ]
            # break loop
            if left_pole == cur_pole:
                break
            # rotate
            pointer[num - cnt] -= direction * (-1) ** cnt
            cnt += 1

        # right
        # cur[2] & right[6]
        cnt = 1
        while num + cnt < 4:
            right_pole = arr[num + cnt][(pointer[num + cnt] + 6) % 8]
            cur_pole = arr[num + cnt - 1][
                (pointer[num + cnt - 1] - direction * (-1) ** cnt + 2) % 8
            ]
            # break loop
            if right_pole == cur_pole:
                break
            # rotate
            pointer[num + cnt] -= direction * (-1) ** cnt
            cnt += 1

    # calculate answer
    answer = 0
    for i in range(4):
        answer += (2**i) * arr[i][pointer[i] % 8]

    print(answer)
