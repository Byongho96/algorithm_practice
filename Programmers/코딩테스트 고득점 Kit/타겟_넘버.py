def solution(numbers, target):
    N = len(numbers)
    answer = 0

    for bit in range(1 << N):
        sm = 0
        for n in range(N):
            if (bit >> n) & 1:
                sm += numbers[n]
            else:
                sm -= numbers[n]
        if sm == target:
            answer += 1

    return answer