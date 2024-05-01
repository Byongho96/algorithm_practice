import sys
input = sys.stdin.readline

answer = 0
counter = [0] * 26
offset = ord('a')

def dfs(N: int, n: int, pre: str):
    global answer 

    if n == N:
        answer += 1
        return 

    for i in range(26):
        if counter[i] == 0:
            continue

        if n == 0 or pre != chr(i+ord('a')):
            counter[i] -= 1
            dfs(N, n+1, chr(i+ord('a')))
            counter[i] += 1

    return 


def solution(string:str) -> int:
    global answer, offset, counter
    answer = 0
    counter = [0] * 26

    # make counter
    for char in string:
        counter[ord(char) - offset] += 1

    dfs(len(string), 0, '')
    return answer
    
if __name__ =="__main__":
    string = input().rstrip()

    answer = solution(string)
    print(answer)