import sys
input = sys.stdin.readline

def solution(a, b):
    return a - b

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(solution(a, b))