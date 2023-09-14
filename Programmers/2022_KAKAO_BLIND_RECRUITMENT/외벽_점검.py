from itertools import permutations


def solution(n, weak, dist):
    W = len(weak)
    weak += [w + n for w in weak]  # extend the weak point twice

    answer = len(dist) + 1
    dist_perm = tuple(permutations(dist))

    # for all start point
    for start in range(W):
        end_pos = weak[start + W - 1]
        for perm in dist_perm:  # test the dist perm
            cnt = 0
            weak_idx = start
            pos = weak[start]
            print(">>")
            for coverage in perm:
                pos += coverage
                cnt += 1
                if start == 0:
                    print(pos, cnt)
                # pruning
                if cnt > answer - 1:
                    break
                # yet covered all the weak points
                if pos < end_pos:
                    while weak[weak_idx] < pos + 1:  # update the next start position
                        weak_idx += 1
                    pos = weak[weak_idx]
                # covered all the weak points
                else:
                    answer = min(answer, cnt)
                    break

    if answer == len(dist) + 1:
        return -1
    else:
        return answer


if __name__ == "__main__":
    print(solution(6, [1, 2, 4, 5], [1, 1]))
