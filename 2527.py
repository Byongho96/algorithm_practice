for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if p1 < x2 or p2 < x1: # x 축이 겹치지 않는 경우
        print('d')
    elif p1 == x2 or p2 == x1:   # x 축이 똑같은 경우
        if q1 < y2 or q2 < y1:
            print('d')
        elif q1 == y2 or q2 == y1:
            print('c')
        else:
            print('b')
    else: # x축이 포함관계인 경우
        if q1 < y2 or q2 < y1:
            print('d')
        elif q1 == y2 or q2 == y1:
            print('b')
        else:
            print('a')