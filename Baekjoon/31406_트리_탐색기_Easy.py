import sys
from typing import Tuple, List

input = sys.stdin.readline

def find_node(leaves: List[List[int]], is_open: List[bool], cur:int, move: int) -> Tuple[bool, int, int]:
    if move == 0:
        return (True, 0, cur)

    if not is_open[cur]:
        return (False, move, cur)
    
    for leaf in leaves:
        move -= 1
        found, move, node = find_node(leaves, is_open, leaf, move)
        if found:
            return (True, move, node)

    return (False, move, node)


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

        if cur_move < 2:
            cur_move = 2
            cur_node = leaves[1][0]
        
        else:
            found, move, node = find_node(leaves, is_open, 0, cur_move)
            cur_move -= move
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