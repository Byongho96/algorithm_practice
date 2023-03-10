from collections import defaultdict
import sys
read = sys.stdin.readline

month_to_date = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

if __name__ == '__main__':
    # 상숫값 input
    N, D, FINE = read().rstrip().split()

    N = int(N)
    FINE = int(FINE)
    DURATION = int(D[:3]) * 24 * 60 + int(D[4:6]) * 60 + int(D[7:])
    
    fines = defaultdict(int)    # {이름: 벌금 누적액}
    book = {}                   # {이름_부품: 빌린 시각(분)}
    for _ in range(N):
        date, time, part, nickname = read().rstrip().split()
        month, days = int(date[5:7]), int(date[8:])
        hours, minutes = int(time[:2]), int(time[3:])
        timestamp = month_to_date[month] * 24 * 60  + days * 24 * 60 + hours * 60 + minutes   # (days-1)로 계산할 경우, 틀렸습니다
        borrowed_timestamp = book.pop(f'{nickname}_{part}', None)

        if borrowed_timestamp:  # 빌린 기록이 있다면 -> 반납
            time_delta = timestamp - borrowed_timestamp
            if time_delta > DURATION:
                fines[nickname] += (time_delta - DURATION) * FINE
        else:                   # 빌린 기록이 없다면 -> 대출
            book[f'{nickname}_{part}'] = timestamp
    
    if fines:
        for name_fine in sorted(list(fines.items())):
            print(*name_fine)
    else:
        print(-1)


# from collections import defaultdict
# import sys
# input = sys.stdin.readline

# month = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
# rental_dic = {}
# fine_dic = defaultdict(int)

# def minute_trans(D, H, m, M = 0):
#     D += month[M]
#     H += D * 24
#     m += H * 60
#     return m

# N, L, F = input().rstrip().split()
# N = int(N)
# D_lm = int(L[:3])
# H_lm = int(L[4:6])
# m_lm = int(L[7:])
# F = int(F)
# duration_lm = minute_trans(D_lm, H_lm, m_lm)

# for _ in range(N):
#     YMD, HM, equip, name = input().rstrip().split()
#     M_e = int(YMD[5:7])
#     D_e = int(YMD[8:])
#     H_e, m_e = map(int, HM.split(':'))
#     time_e = minute_trans(D_e, H_e, m_e, M_e)

#     if not rental_dic.get((equip, name)):
#         rental_dic[(equip, name)] = time_e
#     else:
#         time_s = rental_dic.pop((equip, name))      # pop해서 기록을 없애줘야 함!!!!!!!!!!!!!!!!!!!
#         duration = time_e - time_s
#         if duration >= duration_lm + 1:
#             fine = (duration - duration_lm) * F
#             fine_dic[name] += fine

# if fine_dic:
#     fine_lst = sorted(list(fine_dic.items()))
#     for ele in fine_lst:
#         print(*ele)
# else:
#     print(-1)


