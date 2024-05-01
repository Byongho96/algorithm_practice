import sys
input = sys.stdin.readline

def solution(N, men, women):
    men.sort()
    women.sort()

    mi, wi = 0, N -1
    couples = 0
    while mi < N and wi > -1:
        man = men[mi]
        woman = women[wi]

        if man < 0 and woman > 0:
            if abs(man) > woman:
                couples += 1
                mi += 1
                wi -= 1
            else:
                wi -= 1
        elif man > 0 and woman < 0:
            if man < abs(woman):
                couples += 1
                mi += 1
                wi -= 1
            else:
                wi -= 1
        elif man < 0  and woman < 0:
            mi += 1
        else: # man > 0 and woman > 0:
            wi -=1

    return couples
    

if __name__ == "__main__":
    N = int(input())
    men = list(map(int, input().split()))
    women = list(map(int, input().split()))

    answer = solution(N, men, women)
    print(answer)