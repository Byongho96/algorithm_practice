def decimal_changer(num, base):
    int_num = 0
    for c in num:
        int_num = int_num * base
        try:
            int_num += int(c)
        except ValueError:
            int_num += (ord(c) - 55)
    return int_num

N, B = input().split()
print(decimal_changer(N, int(B)))

'''
# <최단시간 코드 참조>
n, b = input().split()

# int(arg, base = 10) 내장함수에서 arg에 문자열, base에 진법을 숫자로 기입하면, 10진변환 해줌.
print(int(n, int(b)))
'''

'''
# <최단시간 코드 참조2>
l = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 아예 0 ~ Z 까지를 하나의 문자열화

c, b = input().split()
b = int(b)
s = 0

for a in c:     # 입력된 c의 각 문자들을 반복
    s *= b          # 자리올림
    s += l.index(a) # 처음에 만든 문자열에서 인덱스값으로 대응하는 숫자를 가져옴

print(s)
'''