import sys
input =sys.stdin.readline

def solution(T, A, A_lst, B, B_lst):
    A_sum = [0]
    B_sum = [0]
    for i in range(A):
        A_sum.append(A_sum[-1] + A_lst[i])
    for i in range(B):
        B_sum.append(B_sum[-1] + B_lst[i])

    A_dict = {}
    for i in range(A):
        for j in range(i + 1, A + 1):
            if A_sum[j] - A_sum[i] in A_dict:
                A_dict[A_sum[j] - A_sum[i]] += 1
            else:
                A_dict[A_sum[j] - A_sum[i]] = 1

    answer = 0
    for i in range(B):
        for j in range(i + 1, B + 1):
            if T - (B_sum[j] - B_sum[i]) in A_dict:
                answer += A_dict[T - (B_sum[j] - B_sum[i])]

    print(answer)

if __name__ =="__main__":
    T = int(input())

    A = int(input())
    A_lst = list(map(int, input().split()))

    B = int(input())
    B_lst = list(map(int, input().split()))

    answer = solution(T, A, A_lst, B, B_lst)