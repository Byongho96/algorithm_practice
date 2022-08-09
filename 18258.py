'''
import sys

class Queue:
    def __init__(self):
        self.queue = []
        self.len = 0
    def push(self, n):
        self.queue.append(n)
        self.len += 1
    def pop(self):
        if self.len:
            self.len -= 1
            return self.queue.pop(0)
        return -1
    def size(self):
        return self.len
    def empty(self):
        if self.len:
            return 0
        return 1
    def front(self):
        if self.len:
            return self.queue[0]
        return -1
    def back(self):
        if self.len:
            return self.queue[-1]
        return -1

q = Queue()
T = int(sys.stdin.readline())
for _ in range(T):
    cmd = sys.stdin.readline().strip()
    if cmd == 'pop':
        print(q.pop())
    elif cmd == 'size':
        print(q.size())
    elif cmd == 'empty':
        print(q.empty())
    elif cmd == 'front':
        print(q.front())
    elif cmd == 'back':
        print(q.back())
    else:
        cmd = cmd.split()
        q.push(int(cmd[1]))
'''
import sys

q = []
T = int(sys.stdin.readline())
for _ in range(T):
    cmd = sys.stdin.readline().strip()
    if cmd == 'pop':
        print(q.pop(0) if len(q) else -1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print(0 if len(q) else 1)
    elif cmd == 'front':
        print(q[0] if len(q) else -1)
    elif cmd == 'back':
        print(q[-1] if len(q) else -1)
    else:
        cmd = cmd.split()
        q.append(int(cmd[1]))