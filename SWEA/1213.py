# for T in range(10):
#     t = int(input())
#     key = input()
#     string = input()
#
#     cnt = 0 # count
#     for i in range(len(string)-len(key)+1): # key string의 길이를 고려해서 읽을 범위 지정
#         if string[i:i+len(key)] == key: # 순차적으로 읽으며, key string과 같은 값이 나오면
#             cnt += 1    # count++
#     print(f'#{t} {cnt}')

