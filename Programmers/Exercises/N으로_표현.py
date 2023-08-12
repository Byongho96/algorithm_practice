def solution(N, number):
    # Eliminate the case of the number is 0
    if number == 0:
        return 2
    
    answer = 0
    DP = [set() for _ in range(10)]
    
    # Set the initial data
    DP[1].add(N)
    
    for idx in range(2, 10):
        # Check the target number is already generated
        if number in DP[idx - 1]:
            return idx - 1
        # Fill the DP
        digit = 0
        for i in range(idx):
            digit = digit * 10 + N
            DP[idx].add(digit)
            for num in DP[idx - i - 1]:
                DP[idx].update(
                    {num + digit, num - digit, digit - num, 
                     num * digit, num // digit, digit // num})
            # To avoid Zero Division Error
            DP[idx].discard(0)

    return answer if answer else -1