def n_square():
    N = int(input())
    # 처음받은 값을, 초기값으로 설정
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    # N-1번 반복
    for _ in range(N-1):
        x3, y3, z3, x4, y4, z4 = map(int, input().split())
        # 처음 정육면체와 나중 정육면체의 교집합으로 하는 작은 정육면체 형성
        x1 = max(x1, x3)
        y1 = max(y1, y3)
        z1 = max(z1, z3)
        x2 = min(x2, x4)
        y2 = min(y2, y4)
        z2 = min(z2, z4)
        # 작은 정육면체가 실제로 형성되었을 경우, 다음 반복문 실행
        if (x1 < x2) and (y1 < y2) and (z1 < z2):
            continue
        # 작은 정육면체가 형성되지 않았을 경우, 0을 리턴
        else:
            return 0
    # 모든 반복문이 끝나고 형성된 정육면체의 부피를 구함
    return ((x2 - x1) * (y2 - y1) * (z2 - z1))


print(n_square())
