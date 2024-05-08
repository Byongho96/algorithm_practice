import sys

def solution(string: str) -> int:
    mx = 0
    s, e = 0, 1

    # two pointer
    while e < len(string):
        if s + mx > e:  # s == e : optimization
            e += 1
            continue
        if string[s:e] in string[s+1:]:
            mx = max(mx, e - s)
            e += 1
            continue
        s += 1

    return mx

if __name__ == "__main__":
    pattern = sys.stdin.readline().rstrip()
    print(solution(pattern)) 
