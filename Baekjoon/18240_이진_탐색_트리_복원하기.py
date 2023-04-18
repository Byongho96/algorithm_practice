# 참고: https://howtolivelikehuman.tistory.com/240
import sys
from collections import deque

sys.setrecursionlimit(3 * 10**5 *2)

# # 아래 Node 클래스는 시간초과로 인해 사용하지 못함
# class Node:
#     # 생성자 함수
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

def inorder(root, value, left, right, answer):
    # 왼쪽 서브트리 탐색
    if left.get(root):
        value = inorder(left[root], value, left, right, answer)

    # 루트 노드 순서에 대응하는 값을 answer에 삽입
    value += 1
    answer[root] = value

    # 오른쪽 서브트리 탐색
    if right.get(root):
        value  = inorder(right[root], value, left, right, answer)

    return value

if __name__ == "__main__":
    N = int(input())
    depth_lst = list(map(int, input().split()))

    # 1. 트리 생성 가능성 판단
    available_depth = [0] * (N + 1) # 주의!) 아닐 시, 아래 for문에서 IndexError 발생할 수 있음
    available_depth[1] = 2
    for depth in depth_lst:
        if available_depth[depth] < 1:
            print(-1)   # 1-1. 트리생성이 불가능할 경우
            break
        available_depth[depth] -= 1
        available_depth[depth + 1] += 2 # depth = d 인 노드 생성 시, depth = d + 1 인 노드를 2개 더 생성할 수 있다.

    # 2. insert 순서(order)를 값으로 가지는 트리 생성
    else:               # 1-2. 트리생성이 가능한 경우
        left = {}   # Node 클래스를 생성하여 탐색 시 python 시간초과 발생 -> 딕셔너리 생성
        right = {}  # Node 클래스를 생성하여 탐색 시 python 시간초과 발생 -> 딕셔너리 생성
        depth_node = {}     # 시간복잡도를 줄이기 위해, depth마다 자식이 채워지지 않은 node값을 저장
        depth_node[0] = deque([0])  # depth=0 인 루트노트 지정. 루트노드는 항상 첫번째로 insert

        order = 0   # insert 순서
        for depth in depth_lst:
            order += 1
            for parent in depth_node[depth - 1]:  # parent를 탐색하면서 가능한 경우 찾기
                if not left.get(parent):    # 왼쪽이 비어있을 경우
                    left[parent] = order
                    if not depth_node.get(depth):
                        depth_node[depth] = deque([order])
                    else:
                        depth_node[depth].append(order)
                    break
                if not right.get(parent):   # 오른쪽이 비어있을 경우
                    right[parent] = order
                    depth_node[depth].append(order)
                    depth_node[depth - 1].popleft() # 자식이 채워진 parent노드는 pop하여 시간복잡도 줄이기
                    break

        root = 0
        value = 0
        answer = [0] * N
        inorder(root, value, left, right, answer)   # 중위순회하며 answer를 채워넣는다.

        print(*answer)