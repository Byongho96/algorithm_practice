A, B = map(int, input().split())

count = 0
sum = 0

for i in range(1, B+1):
    for j in range(i):
        count += 1
        if A <= count <= B:
            sum += i
    if count > B:
        break

print(sum)

# 1 2 2 3 3 3 4 4 4 4  5  5  5  5  51
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
