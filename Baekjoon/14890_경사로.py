import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # Brute force O(2 * N * N)
    answer = 0
    for _ in range(2):
        for row in arr:
            # simulation
            offset = 1  # offset for placing a slope
            for i in range(1, N):
                cur = row[i]
                pre = row[i - 1]

                if cur == pre:  # flat
                    offset += 1
                    continue

                elif abs(cur - pre) > 1:  # impossible
                    break

                elif cur > pre:  # uphill
                    if offset > L - 1:
                        offset = 1
                        continue
                    else:
                        break

                else:  # downhill
                    if offset > -1:
                        offset = -L + 1
                        continue
                    else:
                        break

            else:
                if offset > -1:
                    answer += 1

        arr = list(zip(*arr))

    print(answer)
