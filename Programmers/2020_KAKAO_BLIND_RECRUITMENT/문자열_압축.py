def solution(s):
    N = len(s)
    mn = N

    # test for each size
    for size in range(1, N // 2 + 1):
        # repeated number & total number length
        num, num_len = 0, 0

        result = N  # maximum
        start, end = 0, size
        while end < N:
            cur_string = s[start:end]
            start += size
            end += size
            next_string = s[start:end]

            # if repeated
            if cur_string == next_string:
                num += 1  # count number
                result -= size  # decrease string
                continue

            # if not repeated
            if num:
                num_len += len(str(num + 1))  # update total number length

            num = 0  # reset number

        # handle the last repeated number value
        if num:
            num_len += len(str(num + 1))

        # calculate result
        result += num_len

        # update minimum value
        if result < mn:
            mn = result

    return mn
