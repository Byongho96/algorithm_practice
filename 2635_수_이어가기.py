# def Backtracking():
#     # 종료조건
#     # 가지치기
#     # 후보군 출력
#     for _ in range(N):


N1 = int(input())
mx = 0
mx_lst = []
for n2 in range(1, N1+1):
    n1 = N1
    cnt = 1
    lst = [N1]
    while n2 >= 0:
        n1, n2 = n2, n1 - n2
        lst.append(n1)
        cnt += 1
    if cnt > mx:
        mx = cnt
        mx_lst = lst

print(mx)
print(*mx_lst)