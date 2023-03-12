import sys
input = sys.stdin.readline

# 조합으로 작은 것부터해서 모든 곡을 커버
# def comb_backtracking(n, cnt, limit):
#     global result
#     global mx
#     if cnt == limit:
#         tt_availables = 0
#         for i in range(N):
#             if visited[i]:
#                 tt_availables |= int(availables[i], 2)
#
#         num_availables = 0
#         for i in range(M):
#             if tt_availables>>i & 1:
#                 num_availables += 1
#         # print(tt_availables)
#         # print(num_availables)
#         if num_availables > mx:
#             mx = num_availables
#             result = cnt
#         return
#     if n >= N:
#         return
#     for i in range(n, N):
#         visited[i] = 1
#         comb_backtracking(i+1, cnt+1, limit)
#         visited[i] = 0

N, M = map(int, input().split())
ref = {}
mx = 0
availables = ['' for _ in range(N)]
for i in range(N):
    _, songs = input().rstrip().split()                         # 기타 이름은 굳이 알 필요 없음
    for j in range(M):                                          # Y는 1, N은 0으로 바꿔줌
        availables[i] += '1' if songs[j] == 'Y' else '0'

mx = 0          # 연주 가능한 최대 곡
result = N      # 기타 갯수

for subset in range(1<<N):                          # 모든 부분집합 고려

    # 부분집합의 기타 갯수, 연주 가능한 곡들 추출
    num_guitar = 0
    possible_song = 0
    for i in range(N):
        if subset >> (N-1-i) & 1:
            num_guitar += 1
            possible_song |= int(availables[i], 2)

    # 연주 가능한 곡의 갯수 추출
    num_song = 0
    for j in range(M):
        if possible_song >> j & 1:
            num_song += 1

    # 결과 업데이트 (곡의 갯수 최대, 기타 갯수 최소)
    if num_song > mx:
        mx = num_song
        result = num_guitar
    elif num_song == mx:
        result = min(result, num_guitar)

if not mx:
    print(-1)
else:
    print(result)
