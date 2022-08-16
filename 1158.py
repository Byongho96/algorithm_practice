from collections import deque

N, K = map(int, input().split())
people = deque([i for i in range(1, N+1)])

lst = []
while people:
    people.rotate(-(K-1))
    lst.append(str(people.popleft()))
print('<'+ ', '.join(lst) + '>')
