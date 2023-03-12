
'''
import sys

T = int(sys.stdin.readline()) # == int(input()). 좀 더 빠르다고 함

for _ in range (T):
    a, b = map(int, sys.stdin.readline().split())   # A, B를 정수로 받음
    com_div = min(a, b) # 최대공약수를 담을 변수
    while True:
        if (a % com_div) or (b % com_div): # com_div로 A, B중 하나라도 나눌 수 없을 때,
            com_div -= 1 # com_div 1 감소 후,
            continue    # A, B 모두 나눌 때까지 반복
        break
    com_mul = a * b // com_div
    print(com_mul)
'''
import sys

# Uclid 함수
def Uclid(n, m):
    big, small =  max(n, m), min(m,n)
    while True:
        if not big % small:
            com_div = small
            break
        else:
            big, small = small, (big % small)
    return com_div

# Main Code
T = int(sys.stdin.readline()) # == int(input()). 좀 더 빠르다고 함

for _ in range (T):
    a, b = map(int, sys.stdin.readline().split())   # A, B를 정수로 받음
    com_div = Uclid(a, b) # 최대공약수를 담을 변수
    com_mul = a * b // com_div
    print(com_mul)