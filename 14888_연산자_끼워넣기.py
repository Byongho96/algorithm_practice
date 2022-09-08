def calculate():
    n1 = nums[0]
    for i in range(M):      # ope_list 읽으면서 n1과 n2의 연산
        n2 = nums[i + 1]
        ope = ope_list[i]
        if ope == 0:        # 덧셈
            n1 += n2
        elif ope == 1:      # 뺄셈
            n1 -= n2
        elif ope == 2:      # 곱셈
            n1 *= n2
        else:               # 나눗셈
            if n1 >= 0:
                n1 //= n2
            else:
                n1 = -(-n1 // n2)
        # print(n1)
    return n1


def backtraking(n):
    global mn
    global mx
    # 종료조건
    if n == M:                  # 연산자 조합이 완성되면
        result = calculate()        # 계산
        if mn > result:             # 최솟값 업데이트
            mn = result
        if mx < result:             # 최댓값 업데이트
            mx = result
        return
    # 후보군 출력
    for i in range(4):
        if operators[i]:        # 사용가능한 연산자 종류
            operators[i] -= 1       # 다음 후보군에서 사용할 데이터 수정
            ope_list[n] = i         # 사용할 연산자 리스트 형성
            backtraking(n + 1)      # 후보군 출력
            operators[i] += 1       # 사용 데이터 복귀


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
M = sum(operators)

mn = 1000000000     # 문제조건의 범위
mx = -1000000000    # 문제조건의 범위
ope_list = [0] * M
backtraking(0)      # 백트래킹

print(mx)
print(mn)
