# https://this-programmer.tistory.com/409
def eratosthenes(N):
    is_prime = [True] * (N + 1)

    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i + i, N + 1, i):
                is_prime[j] = False

    return [i for i in range(2, N + 1) if is_prime[i]]


def eratosthenes_deletion(N, K):
    is_prime = [True] * (N + 1)

    cnt = 0
    for i in range(2, N + 1):
        if is_prime[i]:
            for j in range(i, N + 1, i):
                if not is_prime[j]:
                    continue
                is_prime[j] = False
                cnt += 1
                if cnt == K:
                    return j


if __name__ == "__main__":
    N, K = map(int, input().split())

    answer = eratosthenes_deletion(N, K)
    print(answer)
