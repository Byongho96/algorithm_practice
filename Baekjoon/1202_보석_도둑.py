import sys

input = sys.stdin.readline

# 1. 작은 가방 부터 시작해서
# 2. 가방에 넣을 수 있는 보석 중 가장 비싼 보석을 넣는다.
def solution(N, K, jewels, bags):
    jewels.sort(key=lambda x: -x[1]) # 가치 순으로 내림차순 정렬
    bags.sort()
    collected = [False] * N

    answer = 0
    for bag in bags:
        for idx in range(N):
            if jewels[idx][0] > bag or collected[idx]:
                continue
            collected[idx] = True
            answer += jewels[idx][1]
            break

    return answer

if __name__ == "__main__":
    N, K = map(int, input().split())

    jewels = [list(map(int, input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)]

    answer = solution(N, K, jewels, bags)
    print(answer)