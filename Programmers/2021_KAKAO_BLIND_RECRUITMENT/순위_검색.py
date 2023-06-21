# 처음에는 언어(3개), 직군(2개), 경력(2개), 소울푸드(2개)에 대해 9개의 그룹을 만들고 집합연산을 실행
# 시간초과하여 해설지(https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/)를 보고 최대 4 * 3 * 3 * 3 개의 그룹을 생성

from collections import defaultdict

# 속할 수 있는 모든 그룹이름 반환
def make_groups(language, group, career, food):
    names = [language, group, career, food]
    groups = []
    
    # 16 가지의 경우의 수 존재 : 항목의 원래 이름 or '-'
		# cpp, backend, junior, pizza => ['----', '---pizza', '--junior-', '--juniorpizza', '-backend--', ...]
    for bit in range(1<<4):
        group = ''
        for i in range(4):
            if bit>>(3-i) & 1:
                group += names[i]
            else:
                group += '-'
        groups.append(group)
    
    return groups
                

# 이진탐색으로 구현(동일값이 있을 수 있음을 유의) 
def bi_search(array, target):
    left = 0 
    right = len(array) - 1
    
    target_idx = len(array)
    while left < right + 1:
        middle = (left + right) // 2
        if array[middle] < target:
            left = middle + 1
        else:
            target_idx = middle
            right = middle - 1
    
    return target_idx

def solution(info, query):
    I = len(info)
    Q = len(query)
    answer = []
    groups_dict = defaultdict(list) # 각 그룹에 속한 점수배열을 담고 있음
    
    # 지원자가 속할 수 있는 모든 그룹(리스트)에, 지원자의 점수를 추가
    for i in info:
        language, group, career, food, score = i.split()
        groups = make_groups(language, group, career, food) # 주어진 정보로 만들 수 있는 모든 그룹 리스트 반환
        for group in groups:    # 속할 수 있는 모든 그룹에 대해 점수를 추가
            groups_dict[group].append(int(score))

    # 모든 그룹의 점수배열 오름차순 정렬
    for score_list in groups_dict.values():
        score_list.sort()
    
    # 주어진 쿼리 정보로 그룹 키를 만들고, 
    # 헤당 그룹 리스트에서 점수를 기준으로 이진탐색
    for q in query:
        # 주어진 쿼리 정보로, 그룹 키를 생성: Ex cpp, -, junior, pizza => cpp-juniorpizza
        q = q.replace(' and ', '')
        group, score = q.split() 
        
        # 이진 탐색하여 조건에 맞는 인원을 추림
        target_idx = bi_search(groups_dict[group], int(score))
        num = len(groups_dict[group]) - target_idx
        answer.append(num)
        
    return answer