
n = int(input())

pibo_prev = 0
pibo = 1

if n == 0:
    pibo = 0
elif n == 1:
    pibo =1
else:
    for _ in range(n-1):
        pibo, pibo_prev = (pibo + pibo_prev), pibo

print(pibo)

'''
#최단 코드 참조
n = int(input())

pibo_prev = 0
pibo = 1

for _ in range(n):
    pibo, pibo_prev = (pibo + pibo_prev), pibo
    
print(pibo_prev)
'''

