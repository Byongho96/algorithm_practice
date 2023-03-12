# 가장 높은 블록의 인덱스를 찾는 함수
def max_index(arr):
    i_max = 0
    for i in range(1, len(arr)):
        if arr[i_max] < arr[i]:
            i_max = i
    return i_max
# 가장 낮은 블록의 인덱스를 찾는 함수
def min_index(arr):
    i_min = 0
    for i in range(1, len(arr)):
        if arr[i_min] > arr[i]:
            i_min = i
    return i_min
# 메인함수
for t in range(1,11):
    D = int(input())
    blockLst = list(map(int, input().split()))

    for _ in range(D):  # 블록 옮기기
        blockLst[max_index(blockLst)] -= 1  # 가장 높은 블록 하나 차감
        blockLst[min_index(blockLst)] += 1  # 가장 낮은 블록 하나 증가
    result = blockLst[max_index(blockLst)] - blockLst[min_index(blockLst)]

    print(f'#{t} {result}')