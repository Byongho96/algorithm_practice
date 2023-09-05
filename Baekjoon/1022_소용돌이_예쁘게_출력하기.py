if __name__ == '__main__':
    i1, j1, i2, j2 = map(int, input().split())

    # find numbers
    answer = []
    mx_len = 0
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):

            N = max(abs(i), abs(j)) # the order of the square
            offset_origin = 0   # the offset determined by direction
            offset_line = 0 # the offset from the start of the line

            # right-side
            if j > 0 and -j <= i < j:
                offset_line = -i + j - 1
            # up-side
            elif i < 0 and i <= j < -i:
                offset_origin = 2
                offset_line = -i - j - 1
            # down-side
            elif j < 0 and j < i <= -j:
                offset_origin = 4
                offset_line = i - j - 1
            # left-side
            else:
                offset_origin  = 6
                offset_line = i + j - 1

            num = str(1 + (2 * N - 1) ** 2 + N * offset_origin + offset_line)
            answer.append(num)
            mx_len = max(mx_len, len(num))

    # print the spiral
    i = 0
    for _ in range(i2 - i1 + 1):
        for _ in range(j2 - j1 + 1):
            print(answer[i].rjust(mx_len, ' '), end=' ')
            i += 1
        print('')

