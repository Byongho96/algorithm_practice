def eratosthenes(N):
    is_prime = [True] * (N + 1)

    for i in range(2, int(N * 0.5) + 2):
        if is_prime[i]:
            for j in range(i + i, N + 1, i):
                is_prime[j] = False

    return [i for i in range(2, N + 1) if is_prime[i]]


def find_the_num_of_cases(N):
    # get prime array
    primes = eratosthenes(N)
    P = len(primes)

    # to prevent index error
    primes.append(0)

    # two pointer
    cnt = 0
    s, e = 0, 0
    sm = primes[0]
    while s < e + 1 and e < P:
        if sm == N:
            cnt += 1
            sm -= primes[s]
            s += 1
        elif sm < N:
            e += 1
            sm += primes[e]
        else:
            sm -= primes[s]
            s += 1

    return cnt


if __name__ == "__main__":
    N = int(input())

    answer = find_the_num_of_cases(N)
    print(answer)
