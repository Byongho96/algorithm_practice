def countingSortRef(arr, N):
    ref = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}  # 참조 딕셔너리 형성
    counts = [0] * 10
    result = [0] * N

    for c in arr:   # Counting sort함수. 단, 딕셔너리를 한 번 참조
        counts[ref[c]] += 1
    for i in range(1, 10):
        counts[i] += counts[i-1]
    for c in arr[::-1]:
        counts[ref[c]] -= 1
        result[counts[ref[c]]] = c
    return result

T = int(input())

for t in range(1, T + 1):
    t_num, N = input().split()
    nums = input().split()
    result = countingSortRef(nums, int(N)) # Dictionary를 참조하는 Counting Sort 함수

    print(t_num)
    print(*result)