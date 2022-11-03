# # 메모리 초과
# K = int(input())
#
# num = 0
# len = 1
# while len < K:
#     num = (num << len) | ~num
#     len *= 2
#
# print(num >> (len - K) & 1)


K = int(input())

N = 1
while N < K:
    N *= 2

N //= 2
while :
    K -= N
    N //= 2
if K == 2:
    print(1)
else:
    print(0)

# 0: 1
#
# 1: 0
# 2: 1
# 3: 1
# 4: 0
# 5: 1
# 6: 0
# 7: 0
# 8: 1
# 9: 1
# 10: 0

# 01101001100101101001011001
