import sys

input = sys.stdin.readline


def find_port(par, num):
    while par[num] != num:
        num = par[num]
    return num


if __name__ == "__main__":
    par = [i for i in range(int(input()) + 1)]

    answer = 0
    for _ in range(int(input())):
        num = int(input())
        port = find_port(par, num)

        # not possible
        if not port:
            break

        # dock the plane
        answer += 1

        # update the port array
        prev_port = find_port(par, port - 1)
        par[port], par[num] = prev_port, prev_port

    print(answer)
