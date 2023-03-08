# 448ms
from collections import defaultdict

month_to_minutes = [0,
         24*60 * (0),
         24*60 * (1*31),
         24*60 * (1*31 + 2*28),
         24*60 * (1*31 + 2*28 + 3*31),
         24*60 * (1*31 + 2*28 + 3*31 + 4*30),
         24*60 * (1*31 + 2*28 + 3*31 + 4*30 + 5*31),
         24*60 * (1*31 + 2*28 + 3*31 + 4*30 + 5*31 + 6*30),
         24*60 * (1*31 + 2*28 + 3*31 + 4*30 + 5*31 + 6*30 + 7*31),
         24*60 * (1*31 + 2*28 + 3*31 + 4*30 + 5*31 + 6*30 + 7*31 + 8*31),
         24*60 * (1*31 + 2*28 + 3*31 + 4*30 + 5*31 + 6*30 + 7*31 + 8*31 + 9*30),
         24*60 * (1*31 + 2*28 + 3*31 + 4*30 + 5*31 + 6*30 + 7*31 + 8*31 + 9*30 + 10*31),
         24*60 * (1*31 + 2*28 + 3*31 + 4*30 + 5*31 + 6*30 + 7*31 + 8*31 + 9*30 + 10*31 + 11*30),
         ]

if __name__ == '__main__':
    N, DURATION, FINE = input().split()

    N = int(N)
    FINE = int(FINE)

    DAYS, HOURMINUTES  = DURATION.split('/')
    HOURS, MINUTES = HOURMINUTES.split(':')
    DURATION = int(DAYS) * 24 * 60 + int(HOURS) * 60 + int(MINUTES)
    
    fines = defaultdict(int)
    book = {}
    for _ in range(N):
        date, time, part, nickname = input().split()
        year, month, days = map(int, date.split('-'))
        hours, minutes = map(int, time.split(':'))

        timestamp = month_to_minutes[month] + (days-1) * 24 * 60 + hours * 60 + minutes
        borrowed_timestamp = book.pop(f'{nickname}_{part}', None)
        if borrowed_timestamp:
            time_delta = timestamp - borrowed_timestamp
            if time_delta > DURATION:
                fines[nickname] += (time_delta - DURATION) * FINE
        else:
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

