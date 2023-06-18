from collections import defaultdict, deque
import sys

sys.setrecursionlimit(3 * 10**5 *2)

# class Node:
#     # 생성자 함수
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

def inorder(root, value, left, right, answer):
    # 왼쪽 서브트리
    if left.get(root):
        value = inorder(left[root], value, left, right, answer)
    # 루트 노드에 대응하는 값
    value += 1
    answer[root] = value
    # 오른쪽 서브트리
    if right.get(root):
        value  = inorder(right[root], value, left, right, answer)
    return value

if __name__ == "__main__":
    N = int(input())
    depth_lst = list(map(int, input().split()))

    available_depth = [0] * N
    available_depth[1] = 2

    for depth in depth_lst:
        if available_depth[depth] < 1:
            print(-1)   # 출력 불가능한 경우
            break
        available_depth[depth] -= 1
        available_depth[depth + 1] += 2

    else:               # 출력 가능한 경우, 순서의 값을 저장하는 트리를 만든다.
        left = {}
        right = {}
        depth_node = {}
        depth_node[0] = deque([0])

        order = 0
        for depth in depth_lst:
            order += 1
            for parent in depth_node[depth-1]:
                if not left.get(parent):
                    left[parent] = order
                    if not depth_node.get(depth):
                        depth_node[depth] = deque([order])
                    else:
                        depth_node[depth].append(order)
                    break
                if not right.get(parent):
                    right[parent] = order
                    depth_node[depth].append(order)
                    depth_node[depth-1].popleft()
                    break

        root = 0
        value = 0
        answer = [0] * N
        inorder(root, value, left, right, answer)

        print(*answer)