from collections import deque

if __name__ == '__main__':
    N = int(input())

    cards = deque(range(1, N + 1))

    for _ in range(N-1):
        cards.popleft()
        cards.append(cards.popleft())

    print(cards[0])