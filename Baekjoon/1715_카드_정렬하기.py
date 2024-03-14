import sys
import heapq
from typing import List

input = sys.stdin.readline

def solution(N:int, cards: List[int]):
    # make heap
    heapq.heapify(cards)

    # union the smallest cards recursively
    cnt = 0
    while cards:
        if len(cards) < 2:
            return cnt

        new_cnt = heapq.heappop(cards) + heapq.heappop(cards)
        cnt += new_cnt

        heapq.heappush(cards, new_cnt)

if __name__ == "__main__":
    N = int(input())
    cards = list(int(input()) for _ in range(N))

    answer = solution(N, cards)
    print(answer)