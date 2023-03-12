# 1
# 2 ~ 7 : 2
#            6 * 1 + 1
# 8 ~ 19 : 3
#            6 * 1 + 6 * 2 + 1
# 20 ~ 37 : 4
#            6 * 1 + 6 * 2 + 6 * 3 + 1

n = int(input())
circle = 1
step = 1

while n > circle:
    circle += 6 * step
    step += 1

print(step)