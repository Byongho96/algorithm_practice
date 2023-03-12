def sumLst(arr):
    result = 0
    for ele in arr:
        result += ele
    return result

T = int(input())

for t in range(1, T+1):

    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    for i in range(K):
        for j in range(i+1, N):
            if scores[i] < scores[j]:
                scores[i], scores[j] = scores[j], scores[i]

    maxScr = sumLst(scores[:K])

    print(f'#{t} {maxScr}')