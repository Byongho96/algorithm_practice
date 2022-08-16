import sys
from  collections import deque

class Dequeue:
    def __init__(self):
        self.deque = deque()
        self.N = 0
    def pop(self):
        if self.N:
            self.N -= 1
            return self.deque.popleft()
        else:
            return -1
    def size(self):
        return self.N
    def empty(self):
        return (0 if self.N else 1)
    def front(self):
        return (self.deque[0] if self.N else -1)
    def back(self):
        return (self.deque[-1] if self.N else -1)
    def push(self, X):
        self.deque.append(X)
        self.N += 1

T = int(input())
q = Dequeue()
for _ in range(T):
    cmd = sys.stdin.readline().rstrip()
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
        X = cmd.split()[1]
        q.push(X)