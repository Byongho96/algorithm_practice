import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def my_max(arr):
    mx = arr[-1][1]
    mxIdx = len(arr) - 1
    for i in range(len(arr)):
        if arr[i][1] > mx:
            mx = arr[i][1]
            mxIdx = i
    return arr[mxIdx]

T = int(input())
for t in range(1, T + 1):

    N, M = map(int, input().split())
    pizzas = list(enumerate(map(int, input().split()), start=1))

    q = []

    for pizza in pizzas:        # 모든 피자가 화덕에 들어갈 때까지
        while len(q) == N:          # 화덕에 여유공간이 없다면,
            check = q.pop(0)            # 피자 체크
            cheese = check[1] // 2
            if cheese > 0:              # 아직 안녹았으면, 뒤로 append
                q.append((check[0], cheese))
        q.append(pizza)

    # result = my_max(q)              # 모든 피자가 다 들어간 시점에서, 마지막까지 남는 녀석은 가장 치즈가 많은 놈이 아님!! 몫이 벌져미에 따라서 달라지

    while len(q) != 1:                # 하나 남을 때까지
        check = q.pop(0)
        cheese = check[1] // 2
        if cheese > 0:
            q.append((check[0], cheese))

    print(f'#{t} {q[0][0]}')