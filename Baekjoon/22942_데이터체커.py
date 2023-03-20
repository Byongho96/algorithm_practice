if __name__ == "__main__":
    N = int(input())

    points = []
    for i in range(N):
        x, r = map(int, input().rstrip().split())
        points.append((x-r, 1, i))  # 일부로 원이 시작되는 point의 두번째를 1로 설정
        points.append((x+r, 0, i))  

    points.sort()

    stack = [0] * (2 * N)
    top = -1
    for point in points:
        if point[1] == 1:
            top += 1
            stack[top] = point
        else:
            pop_point = stack[top]
            top -= 1
            if pop_point[-1] != point[-1]:
                print('NO')
                break
    else:
        print('YES')


# 구글링
import sys
input = sys.stdin.readline

N = int(input())
lst = []
stk = [0] * 400000
top = -1

for i in range(N):
    cen, rad = map(int, input().rstrip().split())
    lst.append(((cen-rad), i, 0))
    lst.append(((cen+rad), i, 1))

lst.sort()

for point in lst:
    if not point[2]:
        top += 1
        stk[top] = point
    else:
        stk_point = stk[top]
        if stk_point[1] == point[1]:
            top -= 1
        else:
            print('NO')
            break
else:
    print('YES')
