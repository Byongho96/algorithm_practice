X, Y = map(int, input().split())
row = [0]
column = [0]

for _ in range(int(input())):
    direction, P = map(int, input().split())
    if direction:
        column.append(P)
    else:
        row.append(P)

column += [X]
column.sort()
row += [Y]
row.sort()

max_column = 0
for i in range(1, len(column)):
    span = column[i] - column[i-1]
    if span > max_column:
        max_column = span

max_row = 0
for i in range(1, len(row)):
    span = row[i] - row[i - 1]
    if span > max_row:
        max_row = span

print(max_row * max_column)

