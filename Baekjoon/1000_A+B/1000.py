import sys
input = sys.stdin.readline

def solution(N, M):
    return N + M

if __name__ == "__main__":
    N, M = map(int, input().split())
    answer = solution(N, M)
    
    print(answer)