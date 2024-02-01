import sys

input = sys.stdin.readline

# https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0#:~:text=%EC%A0%95%EB%8B%A4%EA%B0%81%ED%98%95%EC%9D%98%20%EB%84%93%EC%9D%B4%EB%A5%BC%20%EA%B5%AC,%EC%9D%98%20%EC%A4%91%EC%8B%AC%EC%9C%BC%EB%A1%9C%20%EB%AA%A8%EC%9D%B4%EB%8A%94%20%EC%84%A0%EB%B6%84
if __name__ == "__main__":
    x, y = [0, 0], [0, 0]
    N = int(input())

    # Remember the first
    x_0, y_0 = map(int, input().split())
    x[0], y[0] = x_0, y_0

    # Caculate by formula
    acc_1, acc_2 = 0, 0
    cur, prev = 0, 0
    for i in range(1, N):
        cur = i % 2
        prev = 1 - cur
        x[cur], y[cur] = map(int, input().split())
        acc_1 += x[prev] * y[cur]
        acc_2 += y[prev] * x[cur]
    acc_1 += x[cur] * y_0
    acc_2 += y[cur] * x_0

    print(round(abs((acc_1 - acc_2) / 2), 1))
s
