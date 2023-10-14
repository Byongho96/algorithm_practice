import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    # num of plates / a variety of sushi / num of consecutive plates / coupon num
    N, V, K, C = map(int, input().split())

    sushi = [int(input()) for _ in range(N)]
    sushi += sushi[:K]

    # variety of sushi
    variety = defaultdict(int)
    variety[C] = N

    # set initial pointers
    s, e = 0, K - 1
    for i in range(K):
        variety[sushi[i]] += 1

    # move pointers
    answer = len(variety)
    for _ in range(N):
        variety[sushi[s]] -= 1
        if not variety[sushi[s]]:
            variety.pop(sushi[s])
        s += 1
        e += 1
        variety[sushi[e]] += 1
        answer = max(answer, len(variety))

        # end condition
        if answer == V:
            break

    print(answer)
