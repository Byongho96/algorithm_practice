T = int(input())

for t in range(1, T+1):
    bus = [0] * 5001 # [0, 1 ~ 5000] 번째 버스 정류장을 지나는 버스 수 리스트
    N = int(input())

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1): # [A : B+1]의 버스 정류장 버스 수 +1
            bus[i] += 1
    
    P = int(input())
    print(f'#{t}', end='') # print '#n' 
    for _ in range(P):
        print(f' {bus[int(input())]}', end ='') # 입력받은 버스 정류장의 버스 수 출력
    print()