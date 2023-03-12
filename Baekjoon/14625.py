H_s, M_s = map(int, input().split())
H_f, M_f = map(int, input().split())
N = int(input())

count = 0
while True:
    if ((H_s % 10 == N) or (H_s // 10 == N)) or ((M_s % 10 == N) or (M_s // 10 == N)):
        count += 1
    if M_s == M_f and H_s == H_f:
        break
    # 시간 업데이트
    M_s += 1
    if M_s == 60:
        H_s += 1
        M_s = 0

print(count)