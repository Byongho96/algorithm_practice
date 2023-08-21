import sys
input = sys.stdin.readline

def two_pointer(N, solutions, i):
    one = solutions[i]  # the fixed solution

    left = i + 1
    right = N - 1

    approxi = INF
    answer = None
    while left < right:
        another = solutions[left] 
        the_other = solutions[right]
        result = one + another + the_other
        
        # move the index
        if not result:
            return True, 0, (one, another, the_other)
        elif result < 0:
            left += 1
        else:
            right -= 1

        # update the better result
        result = abs(result)
        if result < approxi:
            approxi = result
            answer = (one, another, the_other)

    return False, approxi, answer


if __name__ == '__main__':
    N = int(input())
    solutions = list(map(int, input().split()))

    INF = 1000000000 * N
    solutions.sort()

    approxi = INF
    answer = None
    for i in range(N - 2):
        is_found, result, selected = two_pointer(N, solutions, i)

        # found the ideal result
        if is_found:
            answer = selected 
            break
        
        # update the better result
        if result < approxi:
            approxi = result
            answer = selected

    print(*answer) 