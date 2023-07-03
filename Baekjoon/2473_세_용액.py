import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    solutions = list(map(int, input().split()))
    
    solutions.sort()
    min_value = 1000000000 * 3
    answer = []

    for i in range(N-2):    # 하나의 용액을 모든 경우에 대해서 순회
        left = i + 1
        right = N -1
        while left < right: # 나머지 두개의 용액을 투 포인터로 찾음
            sum_value = solutions[i] + solutions[left] + solutions[right]
            if abs(sum_value) < min_value:
                min_value = abs(sum_value)
                answer = [solutions[i], solutions[left], solutions[right]]
            if sum_value > 0:
                right -= 1
            elif sum_value < 0:
                left += 1
            else:
                break
    
    print(*answer)