import sys

input = sys.stdin.readline

DIRECTION = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북 동 남 서


def clean_the_room(N, M, arr, ri, rj, d):
    visited = [[False] * M for _ in range(N)]
    answer = 0

    while True:
        # 청소
        if not visited[ri][rj]:
            visited[ri][rj] = True
            answer += 1

        # 4방면 탐색
        for _ in range(4):
            d = (d - 1) % 4
            di, dj = DIRECTION[d]  # 반시계 방향 회전
            if arr[ri + di][rj + dj] or visited[ri + di][rj + dj]:
                continue
            # 청소되지 않은 빈 칸이 있을 경우
            ri += di
            rj += dj
            break

        # 청소되지 않은 빈 칸이 없는 경우
        else:
            di, dj = DIRECTION[d]
            ri -= di
            rj -= dj
            if arr[ri][rj]:  # 후진 불가능
                break

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    ri, rj, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = clean_the_room(N, M, arr, ri, rj, d)
    print(answer)
