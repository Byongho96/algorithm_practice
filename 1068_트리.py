# https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-1068%EB%B2%88-%ED%8A%B8%EB%A6%ACPython
import sys
input = sys.stdin.readline

## tree(자식노드 리스)를 만들어서 bfs
def dfs(node):
    global cnt
    # 종료조건
    if not tree[node]:
        cnt += 1
        return
    # 후보군 출력
    for i in range(len(tree[node])):
        if tree[node][i] == D:
            if len(tree[node]) == 1:
                cnt += 1
            else:
                continue
        else:
            dfs(tree[node][i])

N = int(input())
parents = list(map(int, input().rstrip().split()))
D = int(input())
root = -1

# 자식 노드를 담은 tree 리스트 형성
tree = [[] for _ in range(N)]
for i in range(N):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

cnt = 0
if root == D:
    pass
else:
    dfs(root)
print(cnt)

##########################################

# tree(기존 부모 리스트)만을 이용해서 탐색
# https://fre2-dom.tistory.com/155
def dfs(delete):
    # 제거할 노드를 -2로 정의
    tree[delete] = -2

    # 반복문을 통해 제거할 노드의 리프노드를 확인
    for i in range(n):
        if delete == tree[i]:
            # 제거할 리프 노드의 리프 노드를 재귀적으로 탐색
            dfs(i)


n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
d = int(sys.stdin.readline())
cnt = 0

# 노드를 삭제
dfs(d)

# 반복문을 통해 제거할 노드가 아니고 트리에 해당 노드의 리프 노드가 없다면 카운트
for i in range(n):
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)