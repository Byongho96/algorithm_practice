# 참고 글: https://velog.io/@dark6ro/%EB%B0%B1%EC%A4%80-2263%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%88%9C%ED%9A%8C
import sys
sys.setrecursionlimit(10**6)

in_order = []
post_order = []
pre_order = []

def make_pre_order(N, in_start, in_end, post_start, post_end):
    # 분할정복의 종료조건
    if N < 1:
        return
    
    # 포스트 오더의 마지막 변수 -> 인 오더의 루트 값
    root = post_order[post_end]
    pre_order.append(root)

    root_idx = in_order_num_to_idx[root]
    left_size = root_idx - in_start
    right_size = in_end - root_idx

    # 사이즈를 기반으로 in_order와 post_order 시작/끝 인덱스 계산
    make_pre_order(left_size, in_start, root_idx-1, post_start, post_start+left_size-1)
    make_pre_order(right_size, root_idx+1, in_end, post_end-right_size, post_end-1)
    return

if __name__ == "__main__":
    N = int(input())
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))

    # 인오더에서 num -> idx를 찾아주는 배열 (없으면 시간초과)
    in_order_num_to_idx = [0] * (N + 1)
    for i in range(N):
        in_order_num_to_idx[in_order[i]] = i

    make_pre_order(N, 0 , N-1, 0, N-1)
    print(*pre_order)



#####################################################
# # https://ku-hug.tistory.com/135?category=978336

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# # 304 ms
# # postorder와 inorder모두 처음인덱스와 끝인덱스로 넘김
# # search하지 않고 index로 찾을 수 있는 리스트 새로 생성
# N = int(input())
# inorder = list(map(int, input().split()))
# postorder = list(map(int, input().split()))

# def make_tree(in_start, in_end, post_start, post_end):
#     global post_ptr
#     if in_end < in_start or post_end < post_start:
#         return
#     root = postorder[post_end]
#     idx = inorder_idx[root]
#     size = idx - in_start
#     # print('root', root, 'idx', idx, 'size', size)

#     print(root, end=' ')

#     make_tree(in_start, idx-1, post_start, post_start + size -1)
#     make_tree(idx + 1, in_end, post_start + size, post_end -1)

# # idx를 구하는 리스트를 미리 형성
# inorder_idx = [0] * (N + 1)
# for i in range(N):
#     inorder_idx[inorder[i]] = i

# make_tree(0, N-1, 0, N-1)

#####################################################
# 시간초과

# N = int(input())
# inorder = list(map(int, input().split()))
# postorder = list(map(int, input().split()))
#
# def make_tree(start, end):
#     global post_ptr
#     if end >= start:
#         post_ptr -= 1
#         root = postorder[post_ptr]
#         idx = inorder_idx[root]
#         # print('start:', start, 'end:', end, 'ptr:', post_ptr, 'idx:', idx, 'root:', root)
#         rights = make_tree(idx + 1, end)
#         lefts = make_tree(start, idx - 1)
#         return [root] + lefts + rights
#     return []
#
# # idx를 구하는 리스트를 미리 형성
# inorder_idx = [0] * (N + 1)
# for i in range(N):
#     inorder_idx[inorder[i]] = i

# post_ptr = N
# print(*make_tree(0, N-1))