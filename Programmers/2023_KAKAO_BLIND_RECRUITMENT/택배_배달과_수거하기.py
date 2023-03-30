def solution(cap, n, deliveries, pickups):

    path = 0
    remain = 0
    for i in range(n-1, -1, -1):
        box = max(deliveries[i] - remain, 0)
        print(deliveries[i], remain, box, i)
        share = box // cap # 몫
        remainder = box % cap # 나머지
        path += (share + 1) * (i + 1)
        print(i)
        remain = cap - remainder
    return

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))