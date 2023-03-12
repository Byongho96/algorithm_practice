import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

for t in range(1, 11):
    input()
    table = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for j in range(100):
        pre = 0
        for i in range(100):
            if table[i][j]:
                if pre == 1 and table[i][j] == 2:
                    cnt += 1
                pre = table[i][j]

    print(f'#{t} {cnt}')

# 숏코딩
# 문자열변환 -> 0없애기 -> '12'카운트
# for t in range(10):
#     input();b=[''.join(i)for i in zip(*[input().split()for _ in '1'*100])];a=0
#     for i in b:a+=i.replace('0','').count('12')
#     print(f'#{t+1}',a)