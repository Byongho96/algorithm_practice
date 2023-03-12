while True:
    try:
        n, k = map(int, input().split())
        chick, stamp = n, n

        while stamp >= k:
            chick += stamp // k
            stamp = (stamp // k) + (stamp % k)
        print(chick)
            
    except EOFError:    # 더 이상 input이 없을 대 발생하는 error
        break

'''
import sys

for i in sys.stdin:
'''