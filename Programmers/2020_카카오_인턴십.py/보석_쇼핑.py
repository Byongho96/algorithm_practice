# 보석 추가
def add_gem(dic, gem):
    num_gem = dic.get(gem)
    
    if num_gem:
        dic[gem] = num_gem + 1
    else:
        dic[gem] = 1

# 보석 제거
def remove_gem(dic, gem):
    num_gem = dic.get(gem)
    
    if num_gem != 1:
        dic[gem] = num_gem - 1
    else:
        del dic[gem]

def solution(gems):
    gem_set = set(gems)
    total_gem = len(gem_set)
    
    start = 0
    end = 0
    # 현재 내가 가진 보석 목록
    gem_dic = {
        gems[start]: 1
    }
    
    min_start = None
    min_end = None
    min_value = len(gems)
    
    while start < len(gems) - total_gem + 1:
        if len(gem_dic) == total_gem and (end - start) < min_value: # 조건에 맞는 경우
            min_value = end - start
            min_start = start
            min_end = end
            if min_value == total_gem - 1:  # 최적 조건을 찾았을 경우, 바로 종료
                break
            remove_gem(gem_dic, gems[start])
            start += 1
        elif len(gem_dic) < total_gem:  # 보석이 부족한 경우, end += 1
            if end == len(gems) - 1:        
                break
            end += 1
            add_gem(gem_dic, gems[end]) # 보석이 충분한 경우, start += 1
        else:
            remove_gem(gem_dic, gems[start])
            start += 1
        
    answer = [min_start + 1, min_end + 1]
    return answer