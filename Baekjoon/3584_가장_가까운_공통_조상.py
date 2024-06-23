import sys
input = sys.stdin.readline


def solution(N, par, node1, node2):
    node1_par = [False] * (N + 1)

    while node1:
        node1_par[node1] = True
        node1 = par[node1]

    while node2:
        if node1_par[node2]:
            return node2
        node2 = par[node2]
    
    return -1

def main():
    N = int(input())
    par = [0] * (N + 1)
    
    for _ in range(N - 1):
        p, c = map(int, input().split())
        par[c] = p

    node1, node2 = map(int, input().split())
    
    answer = solution(N, par, node1, node2)
    return answer


if __name__ == "__main__":
    T = int(input())

    answers = []
    for _ in range(T):
        answer = main()
        answers.append(answer)

    print(*answers, sep='\n')
