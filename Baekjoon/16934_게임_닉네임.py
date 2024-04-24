# https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%9D%BC%EC%9D%B4-Trie

import sys
from typing import List, Tuple

input = sys.stdin.readline


class Node:
    def __init__(self, key: str):
        self.key = key
        self.cnt = 0
        self.children = {}


class Trie:
    
    def __init__(self):
        self.root = Node('')
    
    def insert(self, word:str) -> Tuple[str, int]:
        node = self.root

        prefix = ''
        prefix_flag = False
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
                if not prefix_flag:
                    prefix += c
                    prefix_flag = True
            else:
                prefix += c
            node = node.children[c]

        node.cnt += 1
        return (prefix, node.cnt) 
    
    def search(self, word) -> bool:
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return bool(node.cnt) 
    

def solution(N: int, names: List[str]) -> List[str]:
    trie = Trie()
    answer = [''] * N 

    for (idx, name) in enumerate(names):
        (prefix, cnt) = trie.insert(name)
        if prefix != name:
            answer[idx] = prefix
        elif cnt < 2:
            answer[idx] = f'{prefix}'
        else:
            answer[idx] = f'{prefix}{cnt}'
            
    return answer

if __name__ == "__main__":
    N = int(input())
    names = [input().rstrip() for _ in range(N)]
    
    answer = solution(N, names)
    print(*answer, sep='\n')