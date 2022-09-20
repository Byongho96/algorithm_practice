import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

point = N - 1                   # 마지막 도시는 알 필요 없음
price = 0
while True:
    mn = 1000000001
    pre_point = point           # 끝지점 저장
    for i in range(pre_point):  # 처음부터 지점까지 스캔
        if oil[i] < mn:             # 최솟값 저장
            mn = oil[i]
            point = i
        if oil[i] == 1:
            break
    price += sum(distance[point:pre_point]) * mn
    if not point:
        break

print(price)
