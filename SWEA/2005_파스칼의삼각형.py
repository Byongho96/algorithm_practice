for T in range(1, int(input()) + 1):

    print(f'#{T}')

    N = int(input())
    preLst = [0, 1]                 # 초기 preList 임의로 부여 -> 더했을 때, 1
    for n in range(1, N+1):         # N개의 줄 출력
        lst = [0] * n                   # 줄 별로 미리 배열 확보
        for i in range(n):              # 각 줄의 데이터 채우기
            lst[i] = preLst[i] +preLst[i+1] # 이전 줄의 preList 데이터로 계산
        print(*lst)                     # print
        preLst = [0] + lst + [0]        # 양옆에 [0]을 추가하여 다음 줄의 계산에 활용