#
T = int(input())
for t in range(1,T+1):
    data = input()
    pipes = 0

    cut = 0
    for i in range(len(data)):
        if data[i] == '(':
            if data[i+1] != ')': # 파이프의 시작점일 경우
                pipes += 1
            else: # 레이저일 경우
                cut += pipes  # 지나가는 모든 파이프의 갯수 +1
        elif data[i] == ')' and data[i-1] != '(': #  파이프의 끝점일 경우
            cut += 1
            pipes -= 1
    print(f'#{t} {cut}')

T = int(input())
for t in range(1, T + 1):
    data = input()
    pipe = []
    pipe_i = 0

    cut = 0
    for i in range(len(data)):
        if data[i] == '(':
            if data[i + 1] != ')':  # 파이프의 시작점일 경우
                pipe.append(1)  # 파이프 추가, 1개부터 시작
                pipe_i += 1
            else:  # 레이저일 경우
                for p_i in range(pipe_i):  # 지나가는 모든 파이프의 갯수 +1
                    pipe[p_i] += 1
        elif data[i] == ')' and data[i - 1] != '(':  # 파이프의 끝점일 경우
            cut += pipe.pop()  # 해당 파이프의 갯수를 컷팅갯수에 더해줌
            pipe_i -= 1

    print(f'#{t} {cut}')