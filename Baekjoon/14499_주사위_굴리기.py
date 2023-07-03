import sys
input = sys.stdin.readline

def roll_dice(cmd):
    global dice_direction
    global TOP, RIGHT, FORWARD
    # 동쪽
    # top = left = (7-right) / right = top / forward = forward
    if cmd == 1:
        dice_direction[TOP], dice_direction[RIGHT]  = 7 - dice_direction[RIGHT],dice_direction[TOP]
    # 서쪽
    # top = right / right = bottom = (7-top) / forward = forward
    elif cmd == 2:
        dice_direction[TOP], dice_direction[RIGHT] = dice_direction[RIGHT], 7 -dice_direction[TOP]
    # 북쪽
    # top = forward / right = right / forward = bottom = (7 -top)
    elif cmd == 3:
        dice_direction[TOP], dice_direction[FORWARD] = dice_direction[FORWARD], 7 -dice_direction[TOP]
    # 남쪽
    # top = backward = (7-forward) / right = right / forward = top
    else:
        dice_direction[TOP], dice_direction[FORWARD] = 7 - dice_direction[FORWARD],dice_direction[TOP]


if __name__ == '__main__':
    N, M, x, y, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    commands = list(map(int, input().split()))

    cmd_direction = (None, (0, 1), (0, -1), (-1, 0), (1, 0))    #  명령어에 따른 주사위 위치 변화
    dice_value = [None, 0, 0, 0, 0, 0, 0]   # 주사위 면에 현재 저장된 값
    TOP = 0
    RIGHT = 1
    FORWARD = 2
    dice_direction = [1, 3, 5]  # 주사위의 현재 방향 [top, right, forward]

    for cmd in commands:
        dx, dy = cmd_direction[cmd]
        nx = x + dx
        ny = y + dy
        
        # 지도 탈출 여부 확인
        if nx < 0 or N - 1 < nx or ny < 0 or M - 1 < ny:
            continue
        
        # 주사위 위치 업데이트
        x = nx 
        y = ny
        # 주사위 방향 업데이트
        roll_dice(cmd)

        # 연산작업
        if not arr[x][y]:
            arr[x][y] = dice_value[7 - dice_direction[TOP]]
        else:
            dice_value[7 - dice_direction[TOP]] = arr[x][y]
            arr[x][y] = 0

        print(dice_value[dice_direction[TOP]])

