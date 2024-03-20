import sys
from typing import List

input = sys.stdin.readline

OFFSET = ord('a')
REQUIRED_ALPHABETS = ('a', 'n', 't', 'i', 'c')


def backtracking(N:int, K: int, words: List[int], k: int, learned: int, start_idx: int) -> int:
    # end condition
    if k == K:
        # calculate local answer
        answer = 0
        for word in words:
            if word | learned == learned:
                answer += 1
        return answer
    
    # pruning
    if (25 - start_idx + 1) < (K - k):   # can learn < remain words
        return 0

    # traverse candidates
    mx = 0
    for idx in range(start_idx, 26):
        # already learned
        if learned & 1 << idx:
            continue

        learned |= 1 << idx
        mx = max(backtracking(N, K, words, k + 1, learned, idx + 1), mx)
        learned &= ~(1 << idx)

        if mx == N:
            return mx
        
    return mx

def solution(N: int, K: int, words: List[str]) -> int:
    # a, n, t, i, c
    if K < 5:
        return 0
    
    if K == 26:
        return N

    # bit mask the words
    words_bit = []
    for word in words:
        bit = 0
        for c in word:
            bit |= 1 << (ord(c) - OFFSET)
        words_bit.append(bit)
    
    # learn the required alphabets 
    learned = 0
    for c in REQUIRED_ALPHABETS:
        learned |= 1 << ord(c) - OFFSET

    # backtracking
    return (backtracking(N, K, words_bit, 5, learned, 1))


if __name__ == "__main__":
    N, K = map(int, input().split())
    words = [input().rstrip() for _ in range(N)]

    answer = solution(N, K, words)
    print(answer)