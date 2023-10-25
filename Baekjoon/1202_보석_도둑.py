import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())

    jewels = [list(map(int, input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)]

    jewels.sort(key=lambda x: -x[0])  # sort by reverse weight
    bags.sort()  # sort by available weight

    answer = 0
    avail_jewels = []
    for bag in bags:
        while jewels and jewels[-1][0] < bag + 1:
            heapq.heappush(avail_jewels, -jewels.pop()[1])
        if avail_jewels:
            answer -= heapq.heappop(avail_jewels)

    print(answer)
