import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**4)    # 노드의 갯수가 10000이므로, 최대 10000의 depth로 재귀호출이 일어나고, 각 depth마다 2개의 재귀호출이 일어난다.

def print_pre_to_post(start, end, pre_order):
    if start > end: # 종료조건
        return
    
    root = pre_order[start] # 루트 노트 값
    break_point = end + 1   # 분할한 노드의 인덱스 찾기
    for i in range(start + 1, end + 1):
        if pre_order[i] > root:
            break_point = i
            break

    print_pre_to_post(start + 1, break_point-1, pre_order)  # 왼쪽 서브트리
    print_pre_to_post(break_point, end, pre_order)  # 오른쪽 서브트리
    print(root)


if __name__ == "__main__":
    # 전위순회 값 받기
    pre_order = []
    while True:
        try:
            pre_order.append(int(input()))
        except:
            break

    start = 0   # 분할한 트리의 첫 노드 인덱스
    end = len(pre_order) - 1    # 분할한 트리의 마지막 노드 인덱스
    print_pre_to_post(start, end, pre_order)