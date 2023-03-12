import sys
# parenthesis의 vaild 여부 판단
def parenValid(pa):
    paStk = []
    for p in pa:
        if p == '(':    # (가 들어갈 때마다, push
            paStk.append(0)
        else:
            try:        # )가 들어오면, pop
                paStk.pop()
                continue
            except:     # )가 과도하게 들어왔을 경우, NO 출력
                return 'NO'
    if paStk:   # (과 과도하게 들어왔을 경우, NO 출력
        return 'NO'
    else:
        return 'YES'

T = int(sys.stdin.readline())
for _ in range(T):   
    pa = sys.stdin.readline().strip() # sys.stdin.readline()으로 받을 경우, 마지막에 /n값도 들어가기 때문에 strip()
    print(parenValid(pa))