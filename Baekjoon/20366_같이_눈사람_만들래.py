import sys
from typing import List

input = sys.stdin.readline

def solution(N:int, diameters:List[int]):
    diameters.sort()

    answer = 2 * 10 ** 9
    for i in range(0, N - 2, 1):
        for j in range(N -1, i + 2, -1):
            first = diameters[i] + diameters[j]

            # two pointer
            k = i + 1
            l = j - 1
            while k < l:
                second = diameters[k] + diameters[l]
                answer = min(abs(first-second), answer)

                # found the best answer
                if answer == 0:
                    return 0
               
                # move pointer
                if first > second:
                    k += 1
                else:
                    l -= 1
            
    return answer

if __name__ =="__main__":
    N = int(input())
    diameters = list(map(int, input().split()))

    answer = solution(N, diameters)
    print(answer)