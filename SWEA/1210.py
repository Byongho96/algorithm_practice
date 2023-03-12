for _ in range(10):
    T = int(input())
    ldr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)] # 0으로 양옆을 감싼다

    # 당첨 지점 찾기
    i = 99
    for j in range(1, 101):
        if ldr[i][j] == 2:
            break

    # 거꾸로 올라가기
    while i:    # 제일 꼭대기에 도착할 때까지
        if not(ldr[i][j-1] or ldr[i][j+1]): # 양 옆에 길이 없으면
            i -= 1 # 위로 이동
        elif ldr[i][j-1]: # 왼쪽에 길이 있을 경우
            while ldr[i][j-1]: # 왼쪽으로 더이상 갈 수 없을 때까지 이동
                j -= 1
            i -= 1  # 이후 위로 한 번 이동
        else: # 오른쪽에 길이 있을 경우
            while ldr[i][j+1]: # 오른쪽으로 더이상 갈 수 없을 때까지 이동
                j += 1
            i -= 1  # 이후 위로 한번 이동

    print(f'#{T} {j-1}')    # 처음에 0으로 감싼거 고려