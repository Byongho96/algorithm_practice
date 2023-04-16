# ...
def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance
    
    rocks.sort() # 돌 정렬
    
    #이분 탐색
    while left <= right: 
        mid = (left + right) // 2 # 중간 값
        
        # 거리의 최솟값을 mid로 만들기 위해 제거한 돌의 갯수
        del_rocks = 0
        prev= 0
        for rock in rocks:
            if rock - prev < mid:  # 돌사이의 거리가 가정한 값보다 작으면 제거한다.
                del_rocks += 1 
            else:                  # 아니라면 그 돌을 새로운 기준으로 세운다.
                prev = rock
        if distance - prev < mid:   # 마지막 거리가 mid보다 작을 경우, 마지막 돌을 하나 더 치운다
            del_rocks += 1
                  
        if del_rocks > n:    # 제거된 돌이 많을 경우 -> 거리 기준을 줄인다.
            right = mid - 1
									           
        else:                # 제거된 돌이 같거나 적을 경우 -> 거리가 더 길 경우를 고려해야한다.
														 # 왜? 돌을 더 제거해도 최소 거리 길이는 동일할 수 있음. 솔직히 잘 모르겠음.
            answer = mid
            left = mid + 1
        
    return answer