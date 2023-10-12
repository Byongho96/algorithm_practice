import sys
from collections import defaultdict, deque

input = sys.stdin.readline


# topology sort
def topology_sort(people, graph, indegree):
    q = deque()
    tree = defaultdict(list)

    # find root
    for person in people:
        if indegree[person]:
            continue
        q.append(person)

    root = q.copy()

    # toplogy sort
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt]:
                continue
            tree[cur].append(nxt)
            q.append(nxt)

    return root, tree


if __name__ == "__main__":
    N = int(input())
    people = input().split()
    people.sort()
    M = int(input())

    # make DAG
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for _ in range(M):
        child, par = input().split()
        graph[par].append(child)
        indegree[child] += 1

    # topplogy sort
    root, tree = topology_sort(people, graph, indegree)

    # print answers
    print(len(root))
    print(*root)
    for person in people:
        tree[person].sort()
        print(person, len(tree[person]), *tree[person])
