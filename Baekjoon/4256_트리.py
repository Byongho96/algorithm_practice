from collections import deque
import sys
sys.setrecursionlimit(10**3)

def make_postorder(preorder, inorder, p_s, p_e, i_s, i_e):
    if p_s > p_e or p_s > N-1 or p_s < 0:   # 분할정복 종료조건
        return

    root = preorder[p_s]    # 루트 노드
    postorder.appendleft(root)  # 포스트 오더임으로 앞에다가 append

    root_idx = inorder_num_to_idx[root]  # 인오더에서 루트 노드의 인덱스
    make_postorder(preorder, inorder, p_s + (root_idx - i_s + 1), p_e, root_idx + 1, i_e)   # 분할정복
    make_postorder(preorder, inorder, p_s + 1, p_s + (root_idx - i_s), i_s, root_idx -1)

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())
        preorder = input().split()
        inorder = input().split()

        inorder_num_to_idx = {} # inorder의 number와 idx를 매칭하는 딕셔너리. 시간 복잡도를 낮춤
        for idx, num in enumerate(inorder):
            inorder_num_to_idx[num] = idx

        postorder=deque()
        make_postorder(preorder, inorder, 0, N-1, 0, N-1)
        print(' '.join(postorder))

# # 556 ms
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     preorder = list(map(int, input().split()))
#     inorder = list(map(int, input().split()))

#     def make_tree(inorder):
#         global pre_ptr
#         if inorder:
#             pre_ptr += 1
#             root = preorder[pre_ptr]
#             idx = inorder.index(root)
#             left = make_tree(inorder[:idx])
#             right = make_tree(inorder[idx + 1:])
#             print(root, end=' ')

#     pre_ptr = -1
#     make_tree(inorder)
#     print()