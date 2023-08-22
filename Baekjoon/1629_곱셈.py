def divide_conquer(a, b, c):
    # end condition
    if b == 1:
        return a % c
    
    divide_result = divide_conquer(a, b//2, c)

    # odd case
    if b % 2:
        return divide_result * divide_result * a % c
    # even case
    else:
        return divide_result * divide_result % c

if __name__ == '__main__':
    A, B, C = map(int, input().split())

    # run the divide conquer
    answer = divide_conquer(A, B, C)

    print(answer)