def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot  = array[0]
    front_arr, back_arr = [], []

    for n in array[1:]:
        if n <= pivot:
            front_arr.append(n)
        else:
            back_arr.append(n)

    return (quick_sort(front_arr) + [pivot] + quick_sort(back_arr) )

T = int(input())

for _ in range(T):
    ls_before = list(map(int, input().split()))
    ls = quick_sort(ls_before)
    print(ls[-3])
    