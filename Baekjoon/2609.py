import sys

A, B = map(int, sys.stdin.readline().split())

# 최대공약수
a, b = A, B
while a % b:
    a, b = b, a % b
com_div = b
print(com_div)

# 최소공배수
com_mul = A * B // com_div
print(com_mul)
