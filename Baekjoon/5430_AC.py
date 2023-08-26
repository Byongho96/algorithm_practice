import sys
input = sys.stdin.readline

def AC(func: str, N: int, arr: list):
    is_reversed = False
    start = 0 
    end = N

    # run the function
    for f in func:
        if f == 'R':
            is_reversed = not is_reversed
            continue

        # f == 'D'
        if is_reversed:
            end -= 1
        else:
            start += 1

        # handle the error
        if start > end:
            return 'error'

    # return the result
    if is_reversed:
        return arr[start: end][::-1]
    else:
        return arr[start: end]


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        func = input().rstrip()
        N = int(input())

        # make arr
        arr = input().rstrip()
        arr = arr[1: -1]
        if arr:
            arr = list(map(int, arr.split(',')))
        else:
            arr = []
        
        # print the reult
        answer = AC(func, N, arr)
        print(str(answer).replace(' ', ''))