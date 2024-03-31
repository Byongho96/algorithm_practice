import sys
input = sys.stdin.readline

def solution(N:int, K:int) -> int:
    original_N = N

    # greedy
    while bin(N).count('1') > K:
        N += 2 ** (len(bin(N)) - bin(N).rfind('1') - 1)    # buy minimum required bottles to reduce '1'

    return N - original_N

if __name__ == "__main__":
    N, K = map(int, input().split())
    
    answer = solution(N, K)
    print(answer)