import sys

sys.setrecursionlimit(10**4)


class Node:
    def __init__(self, node):
        self.val = node[2]
        self.x = node[0]
        self.left = None
        self.right = None


def pre_order(node):
    if not node:
        return []

    answer = [node.val]
    answer.extend(pre_order(node.left))
    answer.extend(pre_order(node.right))

    return answer


def post_order(node):
    if not node:
        return []

    answer = post_order(node.left)
    answer.extend(post_order(node.right))
    answer.append(node.val)


def solution(nodeinfo):
    # add value
    for val, node in enumerate(nodeinfo):
        node.append(val + 1)

    # sort the nodes (from root node)
    nodeinfo.sort(key=lambda x: (-x[1], -x[0]))

    # make tree
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

    return [pre_order(root), post_order(root)]


solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
