import sys
input = sys.stdin.readline

tc = 0
while True:
    tc += 1
    pairs = []
    while True:
        pairs.extend(list(map(int, input().split())))
        if not pairs:
            continue
        if not pairs[-1]:
            pairs.pop()
            pairs.pop()
            break
        if pairs[-1] < 0:
            exit()

    # print('pairs', pairs)

    par = [0] * (max(pairs) + 1)
    for i in range(len(pairs) // 2):
        p, c = pairs[2*i], pairs[2*i+1]
        par[c] = p

    # print('par', par)
    # 1. 루트노드는 부모노드가 없다
    # 2. 그 외 노드는 모두 하나의 부모만 가진다
    # 3. 모든 노드는 루트로부터터 방문가능하다

    print(f'Case {tc} is a tree.')