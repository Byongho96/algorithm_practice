"""
참조
https://velog.io/@jxlhe46/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-%EB%AC%B8%EC%A0%9C
"""
import sys
input = sys.stdin.readline

# fill DP with recursive memoization
def fill_dp_with_memo(cur, visited):
    # base condition
    if visited == END_VISITED :
        if arr[cur][0]:
            return arr[cur][0]
        else:
            return INF

    # use memoitzation
    if DP[visited][cur]:
        return DP[visited][cur]

    # toggle 0 -> INF, for mark as searched 
    DP[visited][cur] = INF

    # set the start
    for nxt in range(N):
        if not arr[cur][nxt]:
            continue
        if visited >> nxt & 1:
            continue
        result = fill_dp_with_memo(nxt, visited | 1 << nxt)
        DP[visited][cur] = min(DP[visited][cur], arr[cur][nxt] + result)

    return DP[visited][cur]

if __name__ == '__main__':
    N = int(input())
    INF = 1000001 * N

    # make arr & set infinite to the unliked edges
    arr = [list(map(int, input().split())) for _ in range(N)]

    # make DP
    # 1 << N == 2 **N
    # DP[visited_node_bit][cur_node]
    DP = [[0] * N for _ in range(1 << N)]

    # fill the DP
    END_VISITED = (1 << N) - 1
    answer = fill_dp_with_memo(0, 1)

    # get the answer
    print(answer)