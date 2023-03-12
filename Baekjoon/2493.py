# 시간 초과
# N = int(input())
# towers = list(enumerate(int, input().split()))
# stk = []*N
#
# mxIdx = [0]
# for i, height in enumerate(towers):
#     for j in range(i, -1, -1):
#         if towers[j] > height:
#             print(j+1, end=' ')
#             break
#     else:
#         print(0, end=' ')

# 신욱님 코드
N = int(input())
towers = list(map(int, input().split()))
stk = [0] * N
ans = [0] * N

top = -1
for i in range(N-1, -1, -1):
    while top != -1 and towers[stk[top]] <= towers[i]:
        ans[stk[top]] = i+1
        top -= 1
    top += 1
    stk[top] = i

print(*ans)