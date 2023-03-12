import sys

fix_cost, var_cost, sales = map(int, sys.stdin.readline().split())  # 입력

if var_cost >= sales:    # 가변비용이 매출액보다 같거나 큰 경우, 손익분기점 X
    print(-1)
else:
    # 손기점 계산 = (고정비용 // (가변비용 - 매출)) + 1
    bep = (fix_cost // (sales - var_cost)) +1 
    print(bep)