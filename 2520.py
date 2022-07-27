T = int(input())

for _ in range(T):
    input()
    mi, y, su, sa, f = map(int, input().split())
    Dough = int(min(mi/8, y/8, su/4, sa, f/9) * 16)
    Ba, St, Ch, Wa = map(int, input().split())
    Topping = Ba + St//30 + Ch//25 + Wa//10
    print(min(Dough, Topping))
