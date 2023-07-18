import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, node):
        self.x = node[0]
        self.y = node[1]
        self.idx = node[2]
        self.left = None
        self.right = None
        
    # 출력 확인용
    def __str__(self):
        return str([self.x, self.y, self.idx])

# 전위 순회
def pre_order(node):
    if not node:
        return []
    
    answer = [node.idx]
    answer.extend(pre_order(node.left))
    answer.extend(pre_order(node.right))
    
    return answer

# 후위 순회
def post_order(node):
    if not node:
        return []
    
    answer = post_order(node.left)
    answer.extend(post_order(node.right))
    answer.append(node.idx)
    
    return answer

def solution(nodeinfo):
    # 인덱스(순서) 달아주기
    for idx, node in enumerate(nodeinfo):
        node.append(idx + 1)
    
    # 정렬
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    
    # 트리 만들기
    root = Node(nodeinfo[0])
    for node in nodeinfo[1:]:
        cur_node = root
        while True:
            if node[0] < cur_node.x:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = Node(node)
                    break
            else:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = Node(node)
                    break
        
    answer = [pre_order(root), post_order(root)]
    return answer