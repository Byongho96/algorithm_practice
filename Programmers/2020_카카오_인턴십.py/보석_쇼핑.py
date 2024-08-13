from collections import defaultdict

def solution(gems):
    N, M = len(gems), len(set(gems))
    collected_dict = defaultdict(int)
    collected_num = 0
    
    def add_gem(gem: str):
        nonlocal collected_num
        if collected_dict[gem] == 0:
            collected_num += 1
        collected_dict[gem] += 1
        
    def remove_gem(gem: str):
        nonlocal collected_num
        collected_dict[gem] -= 1
        if collected_dict[gem] == 0:
            collected_num -= 1

    cur = [0, 0]
    add_gem(gems[0])
    
    mn = N + 1
    answer = [0, 0]

    while True:
        if collected_num == M and cur[1] - cur[0] + 1 < mn:
            mn = cur[1] - cur[0] + 1
            answer[0], answer[1] = cur[0] + 1, cur[1] + 1
    
        if collected_num < M:
            cur[1] += 1
            if cur[1] == N:
                break
            add_gem(gems[cur[1]])
        
        else:
            remove_gem(gems[cur[0]])
            cur[0] += 1        
    
    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])