import sys
from typing import Tuple, List

input = sys.stdin.readline

# recursive function
def find_node(leaves: List[List[int]], is_open: List[bool], cur:int, remain_move: int) -> Tuple[int, int]:
    remain_move -= 1

    # found the target folder
    if remain_move == 0:
        return (0, cur)

    # the folder is closed
    if not is_open[cur]:
        return (remain_move, cur)
    
    # traverse the sub folders
    node = cur
    for leaf in leaves[cur]:
        remain_move, node = find_node(leaves, is_open, leaf, remain_move)
        if not remain_move:
            return (remain_move, node)

    return (remain_move, node)


def solution(N: int, M: int, leaves: List[List[int]], commands: Tuple[List[int]]) -> List[int]:
    answer = []

    # is folder open
    is_open = [False] * (N + 1)
    is_open[1] = True

    cur_move = 1
    cur_node = leaves[1][0]
    for command in commands:
        # toggle
        if len(command) < 2:
            is_open[cur_node] = not is_open[cur_node]
            continue

        # move
        move = int(command[1])
        cur_move += move

        # can't move up more
        if cur_move < 1:
            cur_move = 1
            cur_node = leaves[1][0]
        
        # move the cursoor
        else:
            remain_move, node = find_node(leaves, is_open, 1, cur_move + 1) # +1 is offset for folder 1
            cur_move -= remain_move
            cur_node = node

        answer.append(cur_node)

    return answer
            

if __name__ == "__main__":
    N, M = map(int, input().split())

    # get sub nodes info
    leaves = [0]
    for i in range(1, N + 1):
        _, *arr = map(int, input().split())
        leaves.append(arr)

    # get commmands
    commands = tuple(input().split() for _ in range(M))

    answer = solution(N, M, leaves, commands)
    print(*answer, sep = '\n')