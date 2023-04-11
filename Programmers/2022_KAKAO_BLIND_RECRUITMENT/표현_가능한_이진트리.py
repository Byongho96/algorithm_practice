def traverse_node(root, depth, reverse_visited):
    if depth < 0:
        return
    if not reverse_visited[root]:
        return
    
    reverse_visited[root] = 0 # 방문했을 경우 해당노드를 0으로 만든다
    traverse_node(root - 2 ** (depth - 1), depth - 1, reverse_visited)
    traverse_node(root + 2 ** (depth - 1), depth - 1, reverse_visited)

def isPossible(number):
    # 숫자의 이진수 형태로 만든다
    binary_list = list(map(int, bin(number)[2:]))
    
    # 트리의 너비(N)와 깊이(depth)을 계산한다
    i = 1
    N = 1
    depth = 0
    while True:
        if 1 << N > number:
            break
        N += 2 ** i
        depth += 1
        i += 1
        
    # reverse_visited를 만든다
    reverse_visited = [0] * (N - len(binary_list)) + binary_list
    
    # 루트노드부터 자식 노드를 재귀적으로 탐색해 나간다
    root = N // 2
    traverse_node(root, depth, reverse_visited)
    
    # 모든 노드의 합이 0일 경우 1 반환, 아닐 경우 0 반환
    if sum(reverse_visited):
        return 0
    return 1
    

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(isPossible(number))
    return answer