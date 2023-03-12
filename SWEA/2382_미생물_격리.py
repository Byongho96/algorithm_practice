import sys
sys.stdin = open('input.txt','r',encoding='UTF-8')

dir = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
opposite = {1:3, 2:4, 3:1, 4:2}

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    pos = [[] for _ in range(K)]
    num = [0] * K
    direction = [0] * K

    for idx in range(K):
        i, j, M, D = map(int, input().split())
        pos[idx] = [i, j]
        num[idx] = M
        direction[idx] = D

    # M 시간 후
    for _ in range(M):
        # 모든 미생물 자리 업데이트
        for idx in range(K):
            if num[idx]:
                di, dj = dir[direction[idx]]
                pos[idx][0] += di
                pos[idx][1] += dj

        # 가장자리에 있을 경우
        for idx in range(K):
            if pos[idx][0] == 0 or pos[idx][0] == N-1 or pos[idx][1] == 0 or pos[idx][1] == N-1:
                num[idx] //= 2
                direction[idx] = opposite[direction[idx]]
                if not num[idx]:
                    pos[idx] = 0

        # 같은 자리에 모였을 경우
        positions = {}
        for idx in range(K):
            if pos[idx]:
                position = str(pos[idx][0]) + str(str(pos[idx][1]))
                print(positions, position)
                if position not in positions:
                    positions[position] = [(num[idx], direction[idx], idx)]
                else:
                    positions[position] = positions[position].append((num[idx], direction[idx], idx))
        for position in positions:
            L = len(positions[position])
            if L > 1 :
                lst = positions[position]
                lst.sort(reverse=True)
                total_num = lst[0][0]
                for i in range(1, L):
                    total_num += lst[i][0]
                    num[lst[i][2]] = 0
                    pos[lst[i][2]] = 0
                num[lst[0][2]] = total_num

    print(f'#{tc} {sum(num)}')