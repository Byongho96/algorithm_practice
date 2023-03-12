import sys
data = sys.stdin.readline().rstrip()
pipes = 0

cut = 0
for i in range(len(data)):
    if data[i] == '(':
        if data[i + 1] != ')':  # 파이프의 시작점일 경우
            pipes += 1
        else:  # 레이저일 경우
            cut += pipes  # 지나가는 모든 파이프의 갯수 +1
    elif data[i] == ')' and data[i - 1] != '(':  # 파이프의 끝점일 경우
        cut += 1
        pipes -= 1
sys.stdout(cut + '/n')