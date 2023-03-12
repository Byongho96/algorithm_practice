import sys
T = int(sys.stdin.readline())

stk = []
for _ in range(T):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stk.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(stk.pop() if len(stk) != 0 else -1)
    elif cmd[0] == 'size':
        print(len(stk))
    elif cmd[0] == 'empty':
        print(0 if len(stk) != 0 else 1)
    else:
        print(stk[-1] if len(stk) != 0 else -1)
