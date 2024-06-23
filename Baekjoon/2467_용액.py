INF = 2 * 1000000000 + 1

def solution(N, solutions):
    s, e = 0, N - 1

    mn = INF
    answer = [0, 0]

    while s < e:
        cur = solutions[s] + solutions[e]
        
        if abs(cur) < mn:
            mn = abs(cur)
            answer[0], answer[1] = solutions[s], solutions[e]

        if cur < 0:
            s += 1
        else:
            e -= 1
    
    return answer

if __name__ == "__main__":
    N = int(input())
    solutions = list(map(int, input().split()))

    answer = solution(N, solutions)
    print(*answer)