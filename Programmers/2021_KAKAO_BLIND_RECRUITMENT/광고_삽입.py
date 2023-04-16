# 리스트의 길이가 36만을 넘지 않으며, 순환이 딱 3번 일어난다.

def format_to_seconds(hh_mm_ss):
    hh, mm, ss = map(int, hh_mm_ss.split(':'))
    return hh * 3600 + mm * 60 + ss

def seconds_to_format(seconds):
    hh, mm = divmod(seconds, 3600)
    mm, ss = divmod(mm, 60)
    hh = str(hh) if hh > 9 else '0' + str(hh);
    mm = str(mm) if mm > 9 else '0' + str(mm);
    ss = str(ss) if ss > 9 else '0' + str(ss);
    return hh + ':' + mm + ':' + ss
    
def solution(play_time, adv_time, logs):
    play_time = format_to_seconds(play_time)
    adv_time = format_to_seconds(adv_time)
    
    # 시청자의 유입
    arr = [0] * (play_time + 1)
    for log in logs:
        start, end = map(format_to_seconds, log.split('-'))
        arr[start] += 1
        arr[end] -= 1
    
    # 누적합 1: 현재 시청 밀도
    prev = 0
    cul_arr = [0] * (play_time + 1)
    for i in range(play_time + 1):
        cul_arr[i] = prev + arr[i]
        prev = cul_arr[i]
    
    # 누적합 2: 누적 시청 밀도
    cul_cul_arr = [0] * (play_time + 1)
    for i in range(1, play_time + 1):
        cul_cul_arr[i] = cul_cul_arr[i - 1] + cul_arr[i - 1]
    
    # 누적합 2의 차이로 구간당 시청 밀도를 파악
    answer = 0
    mx = 0
    for i in range(play_time - adv_time + 1):
        density = cul_cul_arr[i + adv_time] - cul_cul_arr[i]
        if density > mx:    # 초과일 때만 업데이트 함으로써, 동일 시청 밀도 중 가장 이른값 파악
            mx = density
            answer = i
    
    return seconds_to_format(answer)